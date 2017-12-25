# UtilizationDataLog

## 1. 資料處理(R)

參考clean.rmd
Step1: 用machine id區別不同machine，並提取該machine每分鐘的資料
Step2: 算出每個machine每分鐘CPU utilization 的最小最大及平均值
Step3: 算出每個machine最大值的變化百分比
Step4: 算出每個machine在一分鐘內出現次數，若超過特定值代表該機器在特定時間使用程度較高，因此他的CPU utilization影響會較大=1, else =0
Step5: sum(每個 machine 最大值變化百分比 ＊ 該machine出現次數category) = y
