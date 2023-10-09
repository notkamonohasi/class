library(gtools)

# 場所の最小値と最大値
MIN_Y = -100
MAX_Y = 100
MIN_X = -100
MAX_X = 100


# 総移動距離を計算する
# input: route: 順番
#        dist_matrix: 距離行列
# return: total_dist: 総移動距離
get_total_dist <- function(route, dist_matrix){
    total_dist <- 0.0
    n <- length(route)
    for(i in 1:(n-1)){
        total_dist <- total_dist + dist_matrix[route[i], route[i + 1]]
    }
    return(total_dist)
}


# 巡回セールスマン問題の「厳密」解を求める
# input: dist_matrix: 距離行列
# return: best_route: 巡回する順番
tsp_exact <- function(dist_matrix){
    n <- nrow(dist_matrix)   # 巡回数
    number_list = seq(2, n, 1)   # 1は最初と最後で決まっているので
    all_combination <- permutations(n=n-1, r=n-1, v=number_list)   # ライブラリで全組合せを列挙する
    best_total_dist <- 1e10
    best_route <- c()
    for(i in 1:nrow(all_combination)){
        route <- c(1, all_combination[i, ], 1)   # 最初と最後にスタート地点を入れておく
        total_dist <- get_total_dist(route, dist_matrix)
        if(best_total_dist > total_dist){
            best_total_dist <- total_dist
            best_route <- route
        }
    }

    return(best_route)
}


# 巡回セールスマン問題の「近似」解を求める
# input: dist_matrix: 距離行列
# return: best_route: 巡回する順番
tsp_approximate <- function(dist_matrix){
    n <- nrow(dist_matrix)   # 巡回数
    pos <- 1   # 今の場所
    visit_list <- c()   # 巡回したindexを入れておく
    while(length(visit_list) != n){
        best_index <- -1   # posから最も近い場所のindex
        best_dist <- 1e10   # posとの最短距離
        for(i in 1:n){
            # 最後以外でスタート地点に戻ることは許されない
            if(i == 1 && length(visit_list) != n - 1){
                next
            }

            # 既に訪れたなら無視する
            else if(i %in% visit_list){
                next
            }

            # 最短となるindexを計算
            else if(best_dist > dist_matrix[pos, i]){
                best_dist <- dist_matrix[pos, i]
                best_index <- i 
            }
        }

        # 状態を更新
        visit_list <- c(visit_list, best_index)
        pos <- best_index
    }

    best_route <- c(1, visit_list)   
    return(best_route)
}


# 乱数を生成する
# input: n: 場所数
# return: place_list: 場所のリスト
make_random_place_list <- function(n){
    ret = matrix(data=0, nrow=n, ncol=2)

    # 同じ地点が出てくる可能性もあるが、可能性は十分小さいので無視する
    for(i in 1:n){
        ret[i,1] <- sample(MIN_X:MAX_X, 1)
        ret[i,2] <- sample(MIN_Y:MAX_Y, 1)
    }
    return(ret)
}


# 距離行列を作る
# input: place_list: 場所のリスト
# return: matrix: 距離行列
make_dist_matrix <- function(place_list){
    n = nrow(place_list)
    ret = matrix(data=0, nrow=n, ncol=n)
    for(i in 1:n){
        for(j in 1:n){
            ret[i, j] <- sqrt((place_list[i, 1] - place_list[j, 1]) ^ 2 + (place_list[i, 2] - place_list[j, 2]) ^ 2)
        }
    }
    return(ret)
}


# 結果を可視化
# input: 
# return: 
visualize <- function(place_list, exact_route, approximate_route, episode, ratio){
    # 保存
    name <- paste0("fig/fig_", episode, "_ratio=", ratio, ".png")
    png(name)

    # 初期化
    plot(1, type = "n", xlim = c(MIN_X, MAX_X), ylim = c(MIN_Y, MAX_Y), xlab = "X", ylab = "Y")

    # 点を全て表示
    points(place_list[1, 1], place_list[1, 2], pch=19, col="red")   # スタート地点のみ違う色でポイントを打つ
    for(i in 2:nrow(place_list)){
        points(place_list[i, 1], place_list[i, 2], pch=19, col="black")
    }

    # 線で結ぶ
    for(i in 1:(length(exact_route)-1)){
        # lines(rbind(place_list[exact_route[i], ], place_list[exact_route[i+1], ]), col="red")   # 線が重なると見えなくなるので、消す
        lines(rbind(place_list[approximate_route[i], ], place_list[approximate_route[i+1], ]), col="blue")
    }

    dev.off()
}


# main ==========================================================================================

# パラメータの宣言
MAX_EPISODE <- 1000
N <- 8   # 巡回する数
set.seed(20230727)   # 再現性を確保するため乱数のシードを固定する

# 結果を格納するlistの宣言
exact_list <- c()   # 厳密解
approximate_list <- c()   # 近似解
approximate_ratio_list <- c()   # 近似率

# モンテカルロ
for(episode in 1:MAX_EPISODE){
    print(episode)

    # 場所をランダムに決定
    place_list <- make_random_place_list(N) 

    # 距離行列作成
    dist_matrix <- make_dist_matrix(place_list)

    # TSPを解き、結果を保存
    exact_route <- tsp_exact(dist_matrix)
    exact_score <- get_total_dist(exact_route, dist_matrix)
    approximate_route <- tsp_approximate(dist_matrix)
    approximate_score <- get_total_dist(approximate_route, dist_matrix)
    exact_list <- c(exact_list, exact_score)
    approximate_list <- c(approximate_list, approximate_score)
    approximate_ratio <- approximate_score / exact_score
    approximate_ratio_list <- c(approximate_ratio_list, approximate_ratio)

    # 近似比が大きかったものについて、結果を可視化する
    if(approximate_ratio > 1.35){
        visualize(place_list, exact_route, approximate_route, episode, approximate_ratio)
    }
}

# 確認用に結果を出力しておく
if(FALSE){
    print(length(exact_list))
    print(exact_list)
    cat("\n")
    print(length(approximate_list))
    print(approximate_list)
    cat("\n")
    print(length(approximate_ratio_list))
    print(approximate_ratio_list)
}

# 近似率の統計量
print(summary(approximate_ratio_list))

# 結果を可視化する
png("fig/hist.png")
plot(1)
hist(approximate_ratio_list, 
     xlab="approximate ratio", 
     ylab="frequency", 
     col="blue",
     breaks=seq(1.0, 2.0, 0.05))
# dev.off()
