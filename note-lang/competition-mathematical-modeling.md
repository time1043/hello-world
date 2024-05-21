# 前言

- 定位

  专注解题：思路、python编程

  不管论文：虽然借阅了很多论文、但不管论文写作

  讲课风格：紧凑、逼迫讲课人、不浪费观众的时间；一题一题地过



- 自己研制教程

  试题：[国赛逐道题目](http://www.mcm.edu.cn/html_cn/block/8579f5fce999cdc896f78bca5d4f8237.html)、公示出来的论文

  清洗：[numpy官方文档](https://numpy.org/doc/)、[pandas官方文档](https://pandas.pydata.org/docs/)、[matplotlib官方文档](https://matplotlib.org/stable/index.html)

  算法：[运筹学规划问题](https://algony-tony.github.io/linear-programming/)、[scipy官方文档](https://docs.scipy.org/doc/scipy/)、[statsmodels统计学模型](https://www.statsmodels.org/stable/index.html)；[机器学习算法公式推导](https://github.com/zhulei227/ML_Notes)、[深度学习gnn](https://distill.pub/2021/gnn-intro/)

  (写个爬虫下载试题)
  
- python数学建模常用类库

  `numpy` + mkl (1.20.2)  科学计算和数据分析的基础库

  `scipy` (1.6.2)  numpy基础上的科学计算库

  `sympy` (1.8)  符号计算库

  `pandas` (1.2.4)  numpy基础上的数据分析库

  `matplotlib` (3.4.1)  数据可视化库

  `scikit-learn` (0.24.1)  机器学习库

  `statsmodels` (0.12.2)  scipy统计函数的补充库

  `networkx` (2.5.1)  图论和复杂网络库

  `cvxpy` (1.1.12)  凸优化库

  `nltk` (3.6.1)  自然语言库

  `pil` (pillow 8.2.0)  数字图像处理库



- 应用方向

  股票分析、物流网络





# numpy





# pandas











# matplotlib











# scipy

- 定位

  在numpy基础上的科学计算库
  
  统计、优化、线性代数、傅里叶变换、信号处理、图像处理、常微分方程
  
- [scipy模块](https://docs.scipy.org/doc/scipy/)

  `scipy.cluster` 聚类分析、`scipy.constants` 物理数学常数、`scipy.fftpack` 傅里叶变换、`scipy.integrate` 积分、`scipy.interpolate` 插值、

  `scipy.io` 数据输入输出、`scipy.linalg` 线性代数、`scipy.ndimage` n维图像、`scipy.odr` 正交距离回归、`scipy.optimize` 优化、

  `scipy.signal` 信号处理、`scipy.sparse` 稀疏矩阵、`scipy.spatial` 空间数据结构与算法、`scipy.special` 特殊函数、`scipy.stats` 统计

  



- 安装

  ```
  pip install scipy sympy
  
  ```

  



- 基本功能

- 求解非线性方程组

  `scipy.optimize`: `fsolve` `root` 请求非线性方程(组)的解 

  ```python
  from scipy.optimize import fsolve, root
  
  # 求解非线性方程
  fun44 = lambda x: (x ** 980) - 5.01 * (x ** 979) + 7.398 * (x ** 978) - 3.388 * (x ** 977) - (x ** 3) \
                    + 5.01 * (x ** 2) - 7.398 * x + 3.388
  x1 = fsolve(fun44, 1.5, maxfev=4000)  # 在给定初值1.5附近有一个实根  函数调用4000次
  x2 = root(fun44, 1.5)
  print(f"{x1}\n\n{x2}\n\n")
  
  # 求解非线性方程组 -> F(X)=0 向量函数
  fun44_vec = lambda x: [x[0] ** 2 + x[1] ** 2 - 1, x[0] - x[1]]
  s1 = fsolve(fun44_vec, [1, 1])
  s2 = root(fun44_vec, [1, 1])
  print(f"{s1}\n\n{s2}\n\n")
  
  ```

- 积分

  `scipy.integrate`: 

  对给定函数的数值积分 

  - `quad(func, a, b, args)` 一重积分、`dblquad(func, a, b, gfun, hfun, args)` 二重积分、`tplquad(func, a, b, gfun, hfun, qfun, rfun)` 三重积分
  - `nquad(func, ranges, args)` 多变量积分

  对给定离散点的数值积分 `trapz`

  ```python
  from scipy.integrate import quad
  
  fun46 = lambda x, a, b: a * x ** 2 + b * x
  I1 = quad(fun46, 0, 1, args=(2, 1))
  I2 = quad(fun46, 0, 1, args=(2, 10))
  print("I1 =", I1[0], ", 精度 ", I1[1])
  print("I2 =", I2[0], ", 精度 ", I2[1])
  
  ```

- 最小二乘解

  `scipy.optimize`: `least_squares(fun, x0)` (fun是向量函数)  求非线性方程组最小二乘解

  ```python
  from scipy.optimize import least_squares
  import numpy as np
  
  a = np.loadtxt('data/data2_47.txt')
  x0, y0, d = a[0], a[1], a[2]
  fun47_vec = lambda x: np.sqrt((x0 - x[0]) ** 2 + (y0 - x[1]) ** 2) - d
  s = least_squares(fun47_vec, np.random.rand(2))
  print(s, "\n\n")
  print(s.x)
  
  ```

- 最大模特征值及对应的特征向量

  ```python
  from scipy.sparse.linalg import eigs
  import numpy as np
  
  a = np.array([[1, 2, 3], [2, 1, 3], [3, 3, 6]], dtype=float)
  b, c = np.linalg.eig(a)
  d, e = eigs(a)
  print(f"eigenvalues: \n{d}")
  print(f"eigenvectors: \n{e}")
  
  ```
  
  



- 求极限

  `scipy.misc.derivative(func, x0, dx=1.0, n=1, args=(), order=3)`

  





# sympy

- 符号计算 (计算机代数)

  用计算机推导数学公式

  运行以推断方式进行，不受误差和累计误差问题的影响

  符号计算的速度比较慢

- 应用

  因式分解、化简、微分、积分、解代数方程、解常微分方程







- 初识

  ```
  import sympy as sp
  help(sp)
  dir(sp)
  
  ```

- 定义符号变量和符号函数

  ```python
  import sympy as sym
  
  x, y, z = sym.symbols('x, y, z')  # 定义符号变量 (逗号分隔 或空格分隔)
  f, g = sym.symbols('f, g', cls=sym.Function)  # 定义符号函数
  y = sym.Function('y')  # 定义符号
  
  sym.var('x, y, z')  # 定义符号变量 (逗号分隔 或空格分隔)
  sym.var('f, g', cls=sym.Function)  # 定义符号函数
  
  ```

- 求解符号代数方程(组)

  `S = solve(f, *symbols)` (f为符号方程 symbols为符号变量)

  ```python
  import sympy as sp
  
  sp.var('x1 x2')
  fun50_1 = lambda x1, x2: x1 ** 2 + x2 ** 2 - 1
  fun50_2 = lambda x1, x2: x1 - x2
  s = sp.solve([fun50_1(x1, x2), fun50_2(x1, x2)], [x1, x2])
  print(f"第一组解为：{s[0]}")
  print(f"第二组解为：{s[1]}")
  
  # 定义符号数组
  x = sp.var('x:2')  # x0 x1
  s2 = sp.solve([fun50_1(x[0], x[1]), fun50_2(x[0], x[1])], x)
  print(f"所有解为：{s2}")
  
  ```
  
- 求解矩阵的特征值特征向量

  ```python
  import numpy as np
  import sympy as sp
  
  # a = sp.Matrix([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])
  a = np.eye(4)
  a = np.rot90(a)
  a = sp.Matrix(a)
  print(f"eigenvalues of a: \n{a.eigenvals()}\n")
  print(f"eigenvectors of a: \n{a.eigenvects()}\n")
  
  ```
  
  









# statsmodels







# NetworkX











# torch







# lstm

- 李宏毅















# gnn











# 210907-cumcm-E

- 题目

  





# 230907-cumcm-C











# 230907-cumcm-E









# 230412-MatherCup-C

- 题目

  > C 题 电商物流网络包裹应急调运与结构优化问题
  >
  > 电商物流网络由物流场地（接货仓、分拣中心、营业部等）和物流场地之间的运输线路组成，如图 1 所示。受节假日和“双十一”、“618”等促销活动的影响，电商用户的下单量会发生显著波动，而疫情、地震等突发事件导致物流场地临时或永久停用时，其处理的包裹将会紧急分流到其他物流场地，这些因素均会影响到各条线路运输的包裹数量，以及各个物流场地处理的包裹数量。  
  >
  > 如果能预测各物流场地及线路的包裹数量（以下简称货量），管理者将可以提前安排运输、分拣等计划，从而降低运营成本，提高运营效率。特别地，在某些场地临时或永久停用时，基于预测结果和各个物流场地的处理能力及线路的运输能力，设计物流网络调整方案，将会大大降低物流场地停用对物流网络的影响，保障物流网络的正常运行。
  >
  > 附件 1 给出了某物流网络在 2021-01-01 至 2022-12-31 期间每天不同物流场地之间流转的货量数据，该物流网络有 81 个物流场地，1049 条线路。其中线路是有方向的，比如线路 DC1→DC2 和线路 DC2→DC1 被认为是两条线路。假设每个物流场地的处理能力和每条线路的运输能力上限均为其历史货量最大值。
  >
  > 基于以上背景，请你们团队完成以下问题：  
  >
  > 问题 1：建立线路货量的预测模型，对 2023-01-01 至 2023-01-31 期间每条线路每天的货量进行预测，并在提交的论文中给出线路 DC14→DC10、DC20→DC35、DC25→DC62 的预测结果。
  >
  > 问题 2：如果物流场地 DC5 于 2023-01-01 开始关停，请在问题 1 的预测基础上，建立数学模型，将 DC5 相关线路的货量分配到其他线路使所有包裹尽可能正常流转，并使得 DC5 关停前后货量发生变化的线路尽可能少，且保持各条线路的工作负荷尽可能均衡。如果存在部分日期部分货量没有正常流转，你们的分流方案还应使得 2023-01-01 至 2023-01-31 期间未能正常流转的包裹日累计总量尽可能少。正常流转时，请给出因 DC5 关停导致货量发生变化的线路数及网络负荷情况；不能正常流转时，请给出因 DC5 关停导致货量发生变化的线路数、不能正常流转的货量及网络的负荷情况。  
  >
  > 问题 3：在问题 2 中，如果被关停的物流场地为 DC9，同时允许对物流网络结构进行动态调整（每日均可调整），调整措施为关闭或新开线路，不包含新增物流场地，假设新开线路的运输能力的上限为已有线路运输能力的最大值。请将 DC9 相关线路的货量分配到其他线路，使所有包裹尽可能正常流转，并使得 DC9 关停前后货量发生变化的线路数尽可能少，且保持各条线路的工作负荷尽可能均衡。如果存在部分日期没有满足要求的流转方案，你们的分流方案还应使得 2023-01-01 至 2023-01-31 期间未能正常流转的包裹日累计总量尽可能少。正常流转时，请给出因 DC9 关停导致货量发生变化的线路数及网络负荷情况；不能正常流转时，请给出因 DC9 关停导致货量发生变化的线路数、不能正常流转的货量及网络的负荷情况；同时请给出每天的线路增减情况。
  >
  > 问题 4：根据附件 1，请对该网络的不同物流场地及线路的重要性进行评价；为了改善网络性能，如果打算新增物流场地及线路，结合问题 1 的预测结果，探讨分析新增物流场地应与哪几个已有物流场地之间新增线路，新增物流场地的处理能力及新增线路的运输能力应如何设置？考虑到预测结果的随机性，请进一步探讨你们所建网络的鲁棒性。  
  
  



- 题目分析

  > 电商物流网络由物流场地（接货仓、分拣中心、营业部等）和物流场地之间的运输线路组成，如图 1 所示。受节假日和“双十一”、“618”等促销活动的影响，电商用户的下单量会发生显著波动，而疫情、地震等突发事件导致物流场地临时或永久停用时，其处理的包裹将会紧急分流到其他物流场地，这些因素均会影响到各条线路运输的包裹数量，以及各个物流场地处理的包裹数量。  
  >
  > 如果能预测各物流场地及线路的包裹数量（以下简称货量），管理者将可以提前安排运输、分拣等计划，从而降低运营成本，提高运营效率。特别地，在某些场地临时或永久停用时，基于预测结果和各个物流场地的处理能力及线路的运输能力，设计物流网络调整方案，将会大大降低物流场地停用对物流网络的影响，保障物流网络的正常运行。

  物流网络：节点、边

  影响因素：购物节、突发事件

  题目目标：预测节点和边的货物、整体网络

  > 附件 1 给出了某物流网络在 2021-01-01 至 2022-12-31 期间每天不同物流场地之间流转的货量数据，该物流网络有 81 个物流场地，1049 条线路。其中线路是有方向的，比如线路 DC1→DC2 和线路 DC2→DC1 被认为是两条线路。假设每个物流场地的处理能力和每条线路的运输能力上限均为其历史货量最大值。

  数据

  附件1：2021-2022两年、每天、各节点间流通货物

  81个节点、1049条有向边

  假设

  节点和边的处理能力上限为历史最值

  > 问题 1：建立线路货量的预测模型，对 2023-01-01 至 2023-01-31 期间每条线路每天的货量进行预测，并在提交的论文中给出线路 DC14→DC10、DC20→DC35、DC25→DC62 的预测结果。

  预测：2023年1月、每天、各节点间流通货物

  强调：DC14→DC10、DC20→DC35、DC25→DC62

  >问题 2：如果物流场地 DC5 于 2023-01-01 开始关停，请在问题 1 的预测基础上，建立数学模型，将 DC5 相关线路的货量分配到其他线路使所有包裹尽可能正常流转，并使得 DC5 关停前后货量发生变化的线路尽可能少，且保持各条线路的工作负荷尽可能均衡。如果存在部分日期部分货量没有正常流转，你们的分流方案还应使得 2023-01-01 至 2023-01-31 期间未能正常流转的包裹日累计总量尽可能少。正常流转时，请给出因 DC5 关停导致货量发生变化的线路数及网络负荷情况；不能正常流转时，请给出因 DC5 关停导致货量发生变化的线路数、不能正常流转的货量及网络的负荷情况。  

  1













# 240412-MatherCup-C

- 参考

  庄晓天等，智能供应链：预测算法理论与实战[M]，电子工业出版社，2023.9.



- 题目

  > C题 物流网络分拣中心货量预测及人员排班
  >
  > 电商物流网络在订单履约中由多个环节组成，图1是一个简化的物流网络示意图。其中，分拣中心作为网络的中间环节，需要将包裹按照不同流向进行分拣并发往下一个场地，最终使包裹到达消费者手中。分拣中心管理效率的提升，对整体网络的履约效率和运作成本起着十分重要的作用。
  >
  > 分拣中心的货量预测是电商物流网络重要的研究问题，对分拣中心货量的精准预测是后续管理及决策的基础，如果管理者可以提前预知之后段时间各个分拣中心需要操作的货量，便可以提前对资源进行安排。在此场景下的货量预测目标一般有两个：一是根据历史货量、物流网络配置等信息，预测每个分拣中心每天的货量；二是根据历史货量小时数据，预测每个分拣中心每小时的货量。
  >
  > 分拣中心的货量预测与网络的运输线路有关，通过分析各线路的运输货量，可以得出各分拣中心之间的网络连接关系。当线路关系调整时，可以参考线路的调整信息，得到各分拣中心货量更为准确的预测。
  >
  > 基于分拣中心货量预测的人员排班是接下来要解决的重要问题，分拣中心的人员包含正式工和临时工两种：正式工是场地长期雇佣的人员，工作效率较高；临时工是根据货量情况临时招募的人员，每天可以任意增减，但工作效率相对较低、雇佣成本较高。根据货量预测结果合理安排人员，旨在完成工作的情况下尽可能降低人员成本。针对当前物流网络，其人员安排班次及小时人效指标情况如下：
  >
  > 1)对于所有分拣中心，每天分为6个班次，分别为：00:00-08:00，05:00-13:00，08:00-16:00，12:00-20:00，14:00-22:00，16:00-24:00，每个人员(正式工或临时工)每天只能出勤一个班次；
  >
  > 2)小时人效指标为每人每小时完成分拣的包裹量(包裹量即货量)，正式工的最高小时人效为 25 包裹/小时，临时工的最高小时人效为 20包裹/小时。
  >
  > 该物流网络包括 57 个分拣中心，每个分拣中心过去4个月的每天货量如附件1所示，过去 30 天的每小时货量如附件2所示。基于以上数据，请完成以下问题：
  >
  > 问题1：建立货量预测模型，对57个分拣中心未来 30 天每天及每小时的货量进行预测，将预测结果写入结果表1和表2中。
  >
  > 问题2：过去 90天各分拣中心之间的各运输线路平均货量如附件3所示。若未来 30 天分拣中心之间的运输线路发生了变化，具体如附件4。所示根据附件1-4，请对57个分拣中心未来 30 天每天及每小时的货量进行预测并将预测结果写入结果表3和表4中。
  >
  > 问题3：假设每个分拣中心有60名正式工，在人员安排时将优先使用正式工，若需额外人员将使用临时工。请基于问题2的预测结果建立模型，给出未来 30 天每个分拣中心每个班次的出勤人数，并写入结果表5中。要求在每天的货量处理完成的基础上，安排的人天数(例如 30天每天出200 名员工，则总人天数为 6000)尽可能少，且每天的实际小时人效尽量均衡。
  >
  > 问题4：研究特定分拣中心的排班问题，这里不妨以SC60为例，假设分拣中心 SC60 当前有 200 名正式工，请基于问题2的预测结果建立模型，确定未来 30 天每名正式工及临时工的班次出勤计划，即给出未来 30 天每天六个班次中，每名正式工将在哪些班次出勤，每个班次需要雇佣多少临时工，并写入结果表6中。每名正式工的出勤率(出勤的天数除以总天数30)不能高于 85%，且连续出勤天数不能超过7天。要求在每天货量处理完成的基础上，安排的人天数尽可能少，每天的实际小时人效尽量均衡且正式工出勤率尽量均衡。

  



- 题目分析

  > 电商物流网络在订单履约中由多个环节组成，图1是一个简化的物流网络示意图。其中，分拣中心作为网络的中间环节，需要将包裹按照不同流向进行分拣并发往下一个场地，最终使包裹到达消费者手中。分拣中心管理效率的提升，对整体网络的履约效率和运作成本起着十分重要的作用。
  >
  > 分拣中心的货量预测是电商物流网络重要的研究问题，对分拣中心货量的精准预测是后续管理及决策的基础，如果管理者可以提前预知之后段时间各个分拣中心需要操作的货量，便可以提前对资源进行安排。在此场景下的货量预测目标一般有两个：一是根据历史货量、物流网络配置等信息，预测每个分拣中心每天的货量；二是根据历史货量小时数据，预测每个分拣中心每小时的货量。
  >
  > 分拣中心的货量预测与网络的运输线路有关，通过分析各线路的运输货量，可以得出各分拣中心之间的网络连接关系。当线路关系调整时，可以参考线路的调整信息，得到各分拣中心货量更为准确的预测。
  
  网络 分拣中心 货量预测

  预测目标：历史货量、网络配置 -> 每个分拣中心 每天的货量

  预测目标：历史货量小时数据 -> 每个分拣中心 每小时的货量

  因素变量：网络的运输线路 (**路线调整**)

  > 基于分拣中心货量预测的人员排班是接下来要解决的重要问题，分拣中心的人员包含正式工和临时工两种：正式工是场地长期雇佣的人员，工作效率较高；临时工是根据货量情况临时招募的人员，每天可以任意增减，但工作效率相对较低、雇佣成本较高。根据货量预测结果合理安排人员，旨在完成工作的情况下尽可能降低人员成本。针对当前物流网络，其人员安排班次及小时人效指标情况如下：
  >
  > 1)对于所有分拣中心，每天分为6个班次，分别为：00:00-08:00，05:00-13:00，08:00-16:00，12:00-20:00，14:00-22:00，16:00-24:00，每个人员(正式工或临时工)每天只能出勤一个班次；
  >
  > 2)小时人效指标为每人每小时完成分拣的包裹量(包裹量即货量)，正式工的最高小时人效为 25 包裹/小时，临时工的最高小时人效为 20包裹/小时。
  
  人员排班 (基于货量预测)
  
  正式工和临时工

  六个班次(每人每天一个班次)

  小时人效指标

  > 该物流网络包括 57 个分拣中心，每个分拣中心过去4个月的每天货量如附件1所示，过去 30 天的每小时货量如附件2所示。基于以上数据，请完成以下问题：

  附件1：每个分拣中心、过去4个月的、每天货量 (6955 = 30*4 * 57)

  附件2：过去30天的、每小时货量 (时间分布)

  附件3：过去90天、各分拣中心之间的、各运输线路平均货量

  附件4：未来30天、分拣中心之间的运输线路发生了**变化**

  > 问题1：建立货量预测模型，对57个分拣中心未来 30 天每天及每小时的货量进行预测，将预测结果写入结果表1和表2中。

  预测：57个分拣中心、未来 30 天、每天及每小时的货量

  选型：时间序列分析、随机森林、lstm

  - 时间序列分析（如ARIMA模型）：适用于预测时间序列数据的未来趋势。
  - 机器学习方法（如随机森林、支持向量机）：可以处理非线性关系，并且能够通过特征工程引入物流网络配置等因素。
  
  > 问题2：过去 90天各分拣中心之间的各运输线路平均货量如附件3所示。若未来 30 天分拣中心之间的运输线路发生了变化，具体如附件4。所示根据附件1-4，请对57个分拣中心未来 30 天每天及每小时的货量进行预测并将预测结果写入结果表3和表4中。
  
  预测：57个分拣中心、未来30天、每天及每小时的货量 (**路线调整**)
  
  选型：
  
  思路：
  
  附件1 -> node 57*122 数据
  
  附件3 -> edge 57*57 邻接矩阵 (有权重的)
  
  附件4 -> edge 57*57 邻接矩阵 (没权重的)
  
  > 问题3：假设每个分拣中心有60名正式工，在人员安排时将优先使用正式工，若需额外人员将使用临时工。请基于问题2的预测结果建立模型，给出未来 30 天每个分拣中心每个班次的出勤人数，并写入结果表5中。要求在每天的货量处理完成的基础上，安排的人天数(例如 30天每天出200 名员工，则总人天数为 6000)尽可能少，且每天的实际小时人效尽量均衡。
  
  条件：每个分拣中心有60名正式工；每天货量处理完成、安排的人天数尽可能少、每天实际小时人效尽量均衡
  
  预测：未来30天、每个分拣中心每个班次的出勤人数
  
  选型：
  
  > 问题4：研究特定分拣中心的排班问题，这里不妨以SC60为例，假设分拣中心 SC60 当前有 200 名正式工，请基于问题2的预测结果建立模型，确定未来 30 天每名正式工及临时工的班次出勤计划，即给出未来 30 天每天六个班次中，每名正式工将在哪些班次出勤，每个班次需要雇佣多少临时工，并写入结果表6中。每名正式工的出勤率(出勤的天数除以总天数30)不能高于 85%，且连续出勤天数不能超过7天。要求在每天货量处理完成的基础上，安排的人天数尽可能少，每天的实际小时人效尽量均衡且正式工出勤率尽量均衡。
  
  预测：
  
  选型：
  
  1







- 代码实现

  ```python
  # 算法模型ARIMA
  model = ARIMA(sc48_data['货量'], order=(1, 1, 1))  # 模型参数 自回归项（AR项） 差分（I项） 移动平均项（MA项）
  results = model.fit()  # 训练模型
  print(results.params)  # 模型的参数
  print(results.summary())  # 模型的相关信息
  
  # 预测未来30天的货量
  forecast = results.get_forecast(steps=30)
  forecast_index = forecast.predicted_index[-30:]
  forecast_values = forecast.predicted_mean[-30:]
  forecast_df = pd.DataFrame(forecast_values, index=forecast_index, columns=['货量预测'])
  print(forecast_df)
  
  ```

- 训练集测试集的划分

  ```python
  # 将data1的数据分为训练集和测试集 每个分拣中心中前92条为训练集，剩余为测试集
  train_data = data1.groupby('分拣中心').apply(lambda x: x.iloc[:92])
  test_data = data1.groupby('分拣中心').apply(lambda x: x.iloc[92:])
  test_data.to_csv('data/data1_test.csv')
  train_data.to_csv('data/data1_train.csv')
  # print(train_data.head(20))
  # print(test_data.head(20))
  ```

- 以SC61分拣中心为例 进行ARIMA模型训练

  ```python
  import pandas as pd
  import matplotlib.pyplot as plt
  from sklearn.model_selection import train_test_split
  from statsmodels.tsa.arima.model import ARIMA
  from sklearn.metrics import mean_squared_error
  from math import sqrt
  
  # 设置matplotlib支持中文的字体
  plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字
  plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
  
  
  def read_clean_file(filename, group_field_list):
      # 读取csv文件 gbk编码
      data = pd.read_csv(filename, encoding='gbk')
      # 将csv的日期字段转换为datetime格式
      data['日期'] = pd.to_datetime(data['日期'])
  
      # 对分拣中心字段进行分组
      cleaned_list = []
      grouped = data.groupby('分拣中心')
      for center, group in grouped:
          sorted_group = group.sort_values(by=group_field_list)
          cleaned_list.append(sorted_group)
      cleaned_data = pd.concat(cleaned_list)
      cleaned_data.set_index('日期', inplace=True)
      return cleaned_data
  
  
  file1 = 'data/附件1.csv'
  file2 = 'data/附件2.csv'
  file3 = 'data/附件3.csv'
  file4 = 'data/附件4.csv'
  data1 = read_clean_file(file1, ['日期'])
  
  # 划分训练集和测试集 随机种子
  # data1_train_data, data1_test_data = train_test_split(data1, test_size=0.3, random_state=42)
  
  # 分拣中心字段的枚举值
  center_list = data1['分拣中心'].unique()
  print(center_list)
  rusult_list = []
  
  # 以SC61分拣中心为例 进行ARIMA模型训练
  center_list_item = 'SC61'
  data1_demo_freq = data1[data1['分拣中心'] == center_list_item]
  print(data1_demo_freq.index.dtype)  # 确认索引的数据类型 datetime64[ns]
  
  frequency = 'D'  # 选择日作为频率
  data1_demo_freq.sort_index(inplace=True)  # 确保数据按照日期排序
  data1_demo_freq = data1_demo_freq.asfreq(frequency)  # 设置频率信息
  
  model_SC61 = ARIMA(data1_demo_freq['货量'], order=(2, 1, 2))
  model_fit_demo = model_SC61.fit()
  print(model_fit_demo.summary())
  
  # 预测未来30天每天的货量
  forecast_demo = model_fit_demo.forecast(steps=30).astype(int)
  # print(type(forecast_demo))  # <class 'pandas.core.series.Series'>
  # print(forecast_demo)
  df_result_demo = forecast_demo.reset_index()
  df_result_demo.columns = ['日期', '货量']
  df_result_demo['分拣中心'] = center_list_item
  df_result_demo = df_result_demo[['分拣中心', '日期', '货量']]
  # print(df_result_demo)
  
  df_result_demo.to_csv('data/结果表1.csv', index=False)
  
  # Todo: 绘制预测结果
  
  ```

- 循环

  ```python
  import pandas as pd
  import matplotlib.pyplot as plt
  from sklearn.model_selection import train_test_split
  from statsmodels.tsa.arima.model import ARIMA
  from sklearn.metrics import mean_squared_error
  from math import sqrt
  
  # 设置matplotlib支持中文的字体
  plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字
  plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
  
  
  def read_clean_file(filename, group_field_list):
      # 读取csv文件 gbk编码
      data = pd.read_csv(filename, encoding='gbk')
      # 将csv的日期字段转换为datetime格式
      data['日期'] = pd.to_datetime(data['日期'])
  
      # 对分拣中心字段进行分组
      cleaned_list = []
      grouped = data.groupby('分拣中心')
      for center, group in grouped:
          sorted_group = group.sort_values(by=group_field_list)
          cleaned_list.append(sorted_group)
      cleaned_data = pd.concat(cleaned_list)
      cleaned_data.set_index('日期', inplace=True)
      return cleaned_data
  
  
  file1 = 'data/附件1.csv'
  file2 = 'data/附件2.csv'
  file3 = 'data/附件3.csv'
  file4 = 'data/附件4.csv'
  data1 = read_clean_file(file1, ['日期'])
  
  # 划分训练集和测试集 随机种子
  # data1_train_data, data1_test_data = train_test_split(data1, test_size=0.3, random_state=42)
  
  # 分拣中心字段的枚举值
  center_list = data1['分拣中心'].unique()
  print(center_list)
  rusult1_list = []
  
  for center_list_item in center_list:
      print(center_list_item)
  
      # 以SC61分拣中心为例 进行ARIMA模型训练
      center_list_item = 'SC61'
  
      data1_demo_freq = data1[data1['分拣中心'] == center_list_item]
      # print(data1_demo_freq.index.dtype)  # 确认索引的数据类型 datetime64[ns]
      frequency = 'D'  # 选择日作为频率
      data1_demo_freq.sort_index(inplace=True)  # 确保数据按照日期排序
      data1_demo_freq = data1_demo_freq.asfreq(frequency)  # 设置频率信息
  
      model_SC61 = ARIMA(data1_demo_freq['货量'], order=(2, 1, 2))
      model_fit_demo = model_SC61.fit()
      print(model_fit_demo.summary())
  
      # 预测未来30天每天的货量
      forecast_demo = model_fit_demo.forecast(steps=30).astype(int)
      # print(type(forecast_demo))  # <class 'pandas.core.series.Series'>
      # print(forecast_demo)
      df_result_demo = forecast_demo.reset_index()
      df_result_demo.columns = ['日期', '货量']
      df_result_demo['分拣中心'] = center_list_item
      df_result_demo = df_result_demo[['分拣中心', '日期', '货量']]
      # print(df_result_demo)
      rusult1_list.append(df_result_demo)
  
      break
  
  rusult1_df = pd.concat(rusult1_list, ignore_index=True)
  rusult1_df.to_csv('data/结果表1.csv', index=False)
  
  # Todo: 绘制预测结果
  
  ```
  
  



















