# -3-
计算机作业
#coding:gbk
"""
利用决策树算法进行分类
作者：郑林涛
日期：2020.5.8
"""
 # 调入需要用的库
import pandas as pd          
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb
#%matplotlib inline

# 调入数据
df = pd.read_csv('frenchwine.csv')
df.columns = ['species', 'magnesium','ash','alcalinity_ash','alcohol', 'mailc_acid'  ]

# 查看前5条数据
df.head()
print(df.head()) 

# 查看数据描述性统计信息
df.describe()
print(df.describe())

#数据的可视化 
def scatter_plot_by_category(feat, x, y): 
    alpha = 0.5
    gs = df.groupby(feat)
    cs = cm.rainbow(np.linspace(0, 1, len(gs)))
    for g, c in zip(gs, cs):
        plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)

plt.figure(figsize=(20,5))
plt.subplot(131)
scatter_plot_by_category('species', 'alcohol', 'alcalinity_ash')
plt.xlabel('alcohol')
plt.ylabel('alcalinity_ash')
plt.title('species')
plt.show()

#利用seaborn库绘制三种Iris花不同参数图
plt.figure(figsize=(20, 10)) 
for column_index, column in enumerate(df.columns):
    if column == 'species':
        continue
    plt.subplot(3, 2, column_index + 1)
    sb.violinplot(x='species', y=column, data=df)
plt.show()

# 首先对数据进行切分，即划分出训练集和测试集
from sklearn.cross_validation import train_test_split #调入sklearn库中交叉检验，划分训练集和测试集
all_inputs = df[['alcohol', 'mailc_acid',
                             'ash', 'alcalinity_ash','magnesium']].values
all_species = df['species'].values

(X_train,
 X_test,
 Y_train,
 Y_test) = train_test_split(all_inputs, all_species, train_size=0.8, random_state=1)#80%的数据选为训练集

# 使用决策树算法进行训练
from sklearn.tree import DecisionTreeClassifier #调入sklearn库中的DecisionTreeClassifier来构建决策树

# 定义一个决策树对象
decision_tree_classifier = DecisionTreeClassifier()

# 训练模型
model = decision_tree_classifier.fit(X_train, Y_train)
# 输出模型的准确度
print(decision_tree_classifier.score(X_test, Y_test)) 

# 使用训练的模型进行预测
print(X_test[0:3])
model.predict(X_test[0:3])

# 对结果用中文表示
def a():
	result = []
	for i in model.predict(X_test[0:3]):
		if i == 'Zinfandel':
			result.append('粉仙黛')
		elif i == 'Syrah':
			result.append('西拉')
		elif i == 'Sauvignon':
			result.append('赤霞珠')
	return result

# print(model.predict(X_test[0:3]))#输出测试的结果，即输出模型预测的结果
print(a())
