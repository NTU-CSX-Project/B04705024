# UtilizationDataLog

## 1. 資料處理(R)

參考clean.rmd
1. 用machine id區別不同machine，並提取該machine每分鐘的資料
2. 算出每個machine每分鐘CPU utilization 的最小最大及平均值
3. 算出每個machine最大值的變化百分比
4. 算出每個machine在一分鐘內出現次數，若超過特定值代表該機器在特定時間使用程度較高，因此他的CPU utilization影響會較大=1, else =0
5. sum(每個 machine 最大值變化百分比 ＊ 該machine出現次數category) = y

## 2. 模型建置
1. LSTM model
2. Set Batch Size
3. Result in LSTM(myon).ipynb
