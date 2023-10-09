library(gtools)

# 巡回セールスマン問題の「厳密」解を求める
# input: dist_matrix: 距離行列
# return: 距離
tsp_exact <- function(dist_matrix){
    n <- nrow(dist_matrix)   # 巡回数
    number_list = seq(2, n, 1)   # 1は最初と最後で決まっているので
    all_combination <- permutations(n=n-1, r=n-1, v=number_list)   # ライブラリで全組合せを列挙する
    best_total_dist <- 1e10
    for(i in 1:nrow(all_combination)){
        order <- c(1, all_combination[i, ], 1)   # 最初と最後にスタート地点を入れておく
        total_dist <- 0
        iter_max <- length(order) - 1
        for(j in 1:iter_max){
            total_dist <- total_dist + dist_matrix[order[j], order[j+1]]
        }
        if(best_total_dist > total_dist){
            best_total_dist <- total_dist
        }
    }

    return(best_total_dist)
}


# 巡回セールスマン問題の「近似」解を求める
# input: dist_matrix: 距離行列
# return: 距離
tsp_approximate <- function(dist_matrix){
    n <- nrow(dist_matrix)   # 巡回数
    total_dist <- 0
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
        total_dist <- total_dist + best_dist
        visit_list <- c(visit_list, best_index)
        pos <- best_index
    }

    return(total_dist)
}


# 乱数を生成する
# input: n: 場所数
# return: place_list: 場所のリスト
make_random_place_list <- function(n){
    ret = matrix(data=0, nrow=n, ncol=2)

    # 場所の最小値と最大値
    MIN_Y = -100
    MAX_Y = 100
    MIN_X = -100
    MAX_X = 100

    # スタート地点は原点とする
    ret[1, 0] = 0
    ret[1, 1] = 0

    # 同じ地点が出てくる可能性もあるが、可能性は十分小さいので無視する
    for(i in 2:n){
        ret[i,1] <- sample(MIN_Y:MAX_Y, 1)
        ret[i,2] <- sample(MIN_X:MAX_X, 1)
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


# main ==========================================================================================

# パラメータの宣言
MAX_EPISODE <- 10
N <- 8   # 巡回する数
set.seed(20230727)   # 再現性を確保するため乱数のシードを固定する

# 結果を格納するlistの宣言
exact_list <- c()   # 厳密解
approximate_list <- c()   # 近似解
approximate_ratio_list <- c()   # 近似率

for(episode in 1:MAX_EPISODE){
    print(episode)

    # 場所をランダムに決定
    place_list <- make_random_place_list(N) 

    # 距離行列作成
    dist_matrix <- make_dist_matrix(place_list)

    exact_score <- tsp_exact(dist_matrix)
    approximate_score <- tsp_approximate(dist_matrix)
    exact_list <- c(exact_list, exact_score)
    approximate_list <- c(approximate_list, approximate_score)
    approximate_ratio_list <- c(approximate_ratio_list, approximate_score / exact_score)
}

# 確認用に結果を出力しておく
print(length(exact_list))
print(exact_list)
cat("\n")
print(length(approximate_list))
print(approximate_list)
cat("\n")
print(length(approximate_ratio_list))
print(approximate_ratio_list)

# 結果を可視化する
hist(approximate_ratio_list, 
     xlab="approximate ratio", 
     ylab="frequency", 
     breaks=seq(1.0, 2.0, 0.05))

