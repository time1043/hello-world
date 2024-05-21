import pandas as pd

# pip install pandas openpyxl

pd.set_option('display.max_columns', None)

# 折算关系
subjects_discount = {
    '语文': 1, '数学': 1, '英语': 1, '体育': 1,
    '物理': 0.6, '化学': 0.6,
    '政治': 0.5, '历史': 0.5,
    '生物': 0.3, '地理': 0.3
}
subjects = list(subjects_discount.keys())

# 各科满分 (及格是满分的*0.6)
subjects_full = {
    '语文': 150, '数学': 150, '英语': 150, '体育': 70,
    '物理': 100, '化学': 100,
    '政治': 100, '历史': 100,
    '生物': 100, '地理': 100
}

print("======================================================================================================")
df_info = pd.read_csv("./data/test_ksxx.csv")
df_score = pd.read_csv("./data/test_kscj.csv")
# print("df_info:\n", df_info)
# print("df_score:\n", df_score)

# print(df_info.info(), "\n")  # 43400 rows  43400 not-null
# print(df_score.info(), "\n")  # 43404 rows  43400 not-null
# print(df_info.isnull().sum(), "\n")  # 0
# print(df_score.isnull().sum(), "\n")  # 0

# 查看df_info中存在重复的考生号 (df_score同理)
df_info_id_count = df_info['考生号'].value_counts()
df_info_id_count_dup = df_info_id_count[df_info_id_count > 1]
df_score_id_count = df_score['考生号'].value_counts()
df_score_id_count_dup = df_score_id_count[df_score_id_count > 1]
# print(df_info_id_count_dup, df_score_id_count_dup)  # 5  # 5

# 对于df_info中重复的考生号，保留第一次出现的，删除后面的 (df_score同理)
df_info = df_info.drop_duplicates(subset='考生号', keep='first')
df_score = df_score.drop_duplicates(subset='考生号', keep='first')
# print(df_info)  # 43400 -> 43395
# print(df_score)  # 43404 -> 43399

print("======================================================================================================")
# 列出df_info、df_score中列名为考生号的枚举值
df_info_id = df_info['考生号'].unique()
df_score_id = df_score['考生号'].unique()

# 列出df_info有的、df_score没有的考生号；列出df_score有的、df_info没有的考生号
df_info_id_only = list(set(df_info_id) - set(df_score_id))
df_score_id_only = list(set(df_score_id) - set(df_info_id))
print(df_info_id_only, df_score_id_only)  # []  # [21951722, 63822363, 76290389, 49590743]

# 删除df_score中的df_score_id_only对应的行
df_score = df_score[~df_score['考生号'].isin(df_score_id_only)]
# print(df_score)  # 43399 -> 43395

print("======================================================================================================")
# 查看df_info中，县区代码字段的枚举值；查看df_info中，学校代码字段的枚举值
df_info_area = df_info['县区代码'].unique()
df_info_school = df_info['学校代码'].unique()
print(len(df_info_area), len(df_info_school))  # 15  # 217
# print(df_info_area, "\n", df_info_school)

# 统计每个学校在每个县区的考生数量
df_info_group_school_area = df_info.groupby(['学校代码', '县区代码'])['考生号'].count().reset_index(name='考生数量')
# print(df_info_group_school_area)  # 376

# 确定每个学校最多的考生所在县区
max_students_per_school = df_info_group_school_area.loc[
    df_info_group_school_area.groupby('学校代码')['考生数量'].idxmax()]
# print(max_students_per_school)  # 217

# 创建一个映射，将学校代码映射到最多的考生所在县区代码
school_to_area_map = max_students_per_school.set_index('学校代码')['县区代码'].to_dict()
print(len(school_to_area_map), "\n", school_to_area_map)  # 217
# 使用映射更新df_info
df_info['县区代码'] = df_info.apply(lambda row: school_to_area_map.get(row['学校代码'], row['县区代码']), axis=1)

# check
df_info_group_school_area = df_info.groupby(['学校代码', '县区代码'])['考生号'].count().reset_index(name='考生数量')
# print(df_info_group_school_area)  # 376 -> 217

print("======================================================================================================")
# 折算分数
df_q13 = df_score.copy()
for subject, factor in subjects_discount.items():
    df_q13[subject] = df_score[subject] * factor
# print(df_q13)

# 将每行的语数英...字段进行累加，得到总分字段
df_q13['折算总分'] = df_q13.apply(
    lambda row: sum(row[subject] for subject in subjects), axis=1)
df_score['折算总分'] = df_q13['折算总分'].apply(lambda x: round(x, 2))
# print(df_score)

print("======================================================================================================")
print("======================================================================================================")
print("======================================================================================================")
df_merge_info_score = pd.merge(df_info, df_score, on='考生号')
print(len(df_info), len(df_score), len(df_merge_info_score))  # 43395  # 43395  # 43395

# 以csv形式输出中间结果
df_info.to_csv("./tmp/df_info.csv", index=False)
df_score.to_csv("./tmp/df_score.csv", index=False)
df_merge_info_score.to_csv("./tmp/df_merge_info_score.csv", index=False)

# 在df_merge_info_score，当subjects字段都为0时，认为是缺考，其缺考字段设置为1，否则设置为0
df_merge_info_score['缺考'] = df_merge_info_score.apply(
    lambda row: 1 if sum(row[subject] for subject in subjects) == 0 else 0, axis=1)
df_merge_info_score.to_csv("./tmp/df_merge_info_score.csv", index=False)

# check 查看缺考
df_q22_missing = df_merge_info_score[df_merge_info_score['缺考'] == 1]
# print(df_q22_missing)  # 609

print("======================================================================================================")
print("======================================================================================================")
# 计算每个考生的语数英总分、所有科目成绩累加
df_merge_info_score['语数英总分'] = df_merge_info_score[subjects[:3]].sum(axis=1)
# 计算每个考生的语数英均分率(450；要求以百分比形式，保留两位小数)
df_merge_info_score['语数英三科均分率(%)'] = df_merge_info_score.apply(
    lambda row: round(row['语数英总分'] / 450 * 100, 2), axis=1)
# 计算每个考生的所有科目均分率(800；要求以百分比形式，保留两位小数)
df_merge_info_score['十科均分率(%)'] = df_merge_info_score.apply(
    lambda row: round(row['折算总分'] / 800 * 100, 2), axis=1)
df_merge_info_score.to_csv("./tmp/df_merge_info_score.csv", index=False)

print("======================================================================================================")
# 在df_merge_info_score，判断考生是否优秀(折算总分字段>=640)，优秀为1，否则为0
df_merge_info_score['是否优秀'] = df_merge_info_score.apply(lambda row: 1 if row['折算总分'] >= 640 else 0, axis=1)
df_merge_info_score.to_csv("./tmp/df_merge_info_score.csv", index=False)

print("======================================================================================================")
# 在df_merge_info_score，分别在各个科目中，判断考生是否及格，及格为1，否则为0
for subject, full in subjects_full.items():
    df_merge_info_score[subject + '是否及格'] = df_merge_info_score.apply(
        lambda row: 1 if row[subject] >= full * 0.6 else 0, axis=1)

# df_merge_info_score，对[subject + '是否及格']的各个字段求和，得到一个考生的及格次数
df_merge_info_score['单科及格次数'] = df_merge_info_score[
    list(subject + '是否及格' for subject in subjects_full.keys())].sum(axis=1)
df_merge_info_score.to_csv("./tmp/df_merge_info_score.csv", index=False)

print("======================================================================================================")
print("======================================================================================================")
# 对于每个县区，计算考生数
df_q22_1 = df_merge_info_score['县区代码'].value_counts().reset_index()
df_q22_1.columns = ['县区代码', '考生数']
# 对于每个县区，计算非缺考人数
every_area_missing = df_merge_info_score.groupby('县区代码')['缺考'].sum().reset_index()
every_area_missing.columns = ['县区代码', '缺考人数']
# print(df_q22_1, "\n", every_area_missing)

# 对于每个县区，与考数 = 考生数 - 缺考人数
df_q22 = pd.merge(df_q22_1, every_area_missing, on='县区代码', how='left')
df_q22['与考数'] = df_q22['考生数'] - df_q22['缺考人数']
# 对于每个学校，计算与考率 (与考数除以考生数，要求以百分比形式，保留两位小数)
df_q22["与考率(%)"] = df_q22.apply(lambda row: round(row['与考数'] / row['考生数'] * 100, 2), axis=1)
df_q22.to_csv("./tmp/df_q22.csv", index=False)

print("======================================================================================================")
# 计算每个县区的语数英均分率、所有科目均分率
df_q22_2 = df_merge_info_score.groupby('县区代码')['语数英三科均分率(%)'].mean().reset_index(name='语数英三科均分率(%)')
df_q22_3 = df_merge_info_score.groupby('县区代码')['十科均分率(%)'].mean().reset_index(name='十科均分率(%)')
# 保留两位小数
df_q22_2['语数英三科均分率(%)'] = df_q22_2['语数英三科均分率(%)'].apply(lambda x: round(x, 2))
df_q22_3['十科均分率(%)'] = df_q22_3['十科均分率(%)'].apply(lambda x: round(x, 2))
# print(df_q22_2，"\n", df_q22_3)

df_q22 = pd.merge(df_q22, df_q22_2, on='县区代码', how='left')
df_q22 = pd.merge(df_q22, df_q22_3, on='县区代码', how='left')
df_q22.to_csv("./tmp/df_q22.csv", index=False)

print("======================================================================================================")
# 计算每个县区的优秀率
df_q22_4 = df_merge_info_score.groupby('县区代码')['是否优秀'].mean().reset_index(name='优秀率(%)')
df_q22_4['优秀率(%)'] = df_q22_4['优秀率(%)'].apply(lambda x: round(x * 100, 2))
# print(df_q22_4)
df_q22 = pd.merge(df_q22, df_q22_4, on='县区代码', how='left')
df_q22.to_csv("./tmp/df_q22.csv", index=False)

# 计算每个县区的及格人次
df_q22_5 = df_merge_info_score.groupby('县区代码')['单科及格次数'].sum().reset_index(name='单科及格人次')
# print(df_q22_5)
df_q22 = pd.merge(df_q22, df_q22_5, on='县区代码', how='left')
# 计算每个县区的及格率 (及格人次除以考生数*10，要求以百分比形式，保留两位小数)
df_q22['单科及格率(%)'] = df_q22.apply(lambda row: round(row['单科及格人次'] / (row['与考数'] * 10) * 100, 2), axis=1)
df_q22.to_csv("./tmp/df_q22.csv", index=False)

print("======================================================================================================")
# 对df_q22，四率综合比：（语数英三科均分率+十科均分率）* 0.3 + （优秀率 + 单科及格率）* 0.2。（要求以百分比形式，保留两位小数）
df_q22['四率综合比(%)'] = df_q22.apply(
    lambda row: round(
        (row['语数英三科均分率(%)'] + row['十科均分率(%)']) * 0.3 + (row['优秀率(%)'] + row['单科及格率(%)']) * 0.2, 2),
    axis=1)
# 对df_q22，按综合四率排序
df_q22['排名'] = df_q22['四率综合比(%)'].rank(ascending=False).astype(int)
df_q22 = df_q22.sort_values(by='四率综合比(%)', ascending=False)
df_q22.to_csv("./tmp/df_q22.csv", index=False)

print("======================================================================================================")
# 整理列
df_q22 = df_q22.drop(columns=['缺考人数', '单科及格人次'])
df_q22.to_csv("./tmp/df_q22.csv", index=False)

print("======================================================================================================")
print("======================================================================================================")
# 对于每个学校，计算考生数
df_q23_1 = df_merge_info_score['学校代码'].value_counts().reset_index()
df_q23_1.columns = ['学校代码', '考生数']
# 对于每个学校，计算非缺考人数
every_school_missing = df_merge_info_score.groupby('学校代码')['缺考'].sum().reset_index()
every_school_missing.columns = ['学校代码', '缺考人数']
# print(df_q23_1, every_school_missing)

# 对于每个学校，与考数 = 考生数 - 缺考人数
df_q23 = pd.merge(df_q23_1, every_school_missing, on='学校代码', how='left')
df_q23['与考数'] = df_q23['考生数'] - df_q23['缺考人数']
# 对于每个学校，计算与考率 (与考数除以考生数，要求以百分比形式，保留两位小数)
df_q23["与考率(%)"] = df_q23.apply(lambda row: round(row['与考数'] / row['考生数'] * 100, 2), axis=1)
df_q23.to_csv("./tmp/df_q23.csv", index=False)

print("======================================================================================================")
# 计算每个学校的语数英均分率、所有科目均分率
df_q23_2 = df_merge_info_score.groupby('学校代码')['语数英三科均分率(%)'].mean().reset_index(name='语数英三科均分率(%)')
df_q23_3 = df_merge_info_score.groupby('学校代码')['十科均分率(%)'].mean().reset_index(name='十科均分率(%)')
# 保留两位小数
df_q23_2['语数英三科均分率(%)'] = df_q23_2['语数英三科均分率(%)'].apply(lambda x: round(x, 2))
df_q23_3['十科均分率(%)'] = df_q23_3['十科均分率(%)'].apply(lambda x: round(x, 2))
# print(df_q23_2, df_q23_3)

df_q23 = pd.merge(df_q23, df_q23_2, on='学校代码', how='left')
df_q23 = pd.merge(df_q23, df_q23_3, on='学校代码', how='left')
df_q22.to_csv("./tmp/df_q23.csv", index=False)

print("======================================================================================================")
# 计算每个县区的优秀率
df_q23_4 = df_merge_info_score.groupby('学校代码')['是否优秀'].mean().reset_index(name='优秀率(%)')
df_q23_4['优秀率(%)'] = df_q23_4['优秀率(%)'].apply(lambda x: round(x * 100, 2))
# print(df_q23_4)
df_q23 = pd.merge(df_q23, df_q23_4, on='学校代码', how='left')
df_q23.to_csv("./tmp/df_q23.csv", index=False)

# 计算每个县区的及格人次
df_q23_5 = df_merge_info_score.groupby('学校代码')['单科及格次数'].sum().reset_index(name='单科及格人次')
# print(df_q22_5)
df_q23 = pd.merge(df_q23, df_q23_5, on='学校代码', how='left')
# 计算每个县区的及格率 (及格人次除以考生数*10，要求以百分比形式，保留两位小数)
df_q23['单科及格率(%)'] = df_q23.apply(lambda row: round(row['单科及格人次'] / (row['与考数'] * 10) * 100, 2), axis=1)
df_q23.to_csv("./tmp/df_q23.csv", index=False)

print("======================================================================================================")
# 对df_q23，四率综合比：（语数英三科均分率+十科均分率）* 0.3 + （优秀率 + 单科及格率）* 0.2。（要求以百分比形式，保留两位小数）
df_q23['四率综合比(%)'] = df_q23.apply(
    lambda row: round(
        (row['语数英三科均分率(%)'] + row['十科均分率(%)']) * 0.3 + (row['优秀率(%)'] + row['单科及格率(%)']) * 0.2, 2),
    axis=1)
# 对df_q23，按综合四率排序
df_q23['排名'] = df_q23['四率综合比(%)'].rank(ascending=False).astype(int)
df_q23 = df_q23.sort_values(by='四率综合比(%)', ascending=False)
df_q23.to_csv("./tmp/df_q23.csv", index=False)

print("======================================================================================================")
# 创建县区代码和学校代码的映射关系
df_q23_6 = df_info[["县区代码", "学校代码"]]
map_for_area = {}
for index, row in df_q23_6.iterrows():
    map_for_area[row["学校代码"]] = row["县区代码"]

# 县区代码的枚举值
area_enum = df_q23_6["县区代码"].unique()
print(area_enum)

# 将map_for_area转为df
df_map_for_area = pd.DataFrame(map_for_area.items(), columns=["学校代码", "县区代码"])
# print(df_map_for_area)

# 整理列
df_q23 = df_q23.drop(columns=['缺考人数', '单科及格人次'])
# df_q23左连接df_info，得到每个学校的县区代码
df_q23 = pd.merge(df_q23, df_map_for_area, on='学校代码', how='left')
df_q23.to_csv("./tmp/df_q23.csv", index=False)

# df_23按照县区代码字段进行分组，分别存储到许多个df中
df_q23_result = {}
for area in area_enum:
    df_q23_result[area] = df_q23[df_q23["县区代码"] == area]

# 将最后一系列df_result分别保存到多个csv中
for area in area_enum:
    df_q23_result[area].to_csv("./tmp/df_q23_result_" + str(area) + ".csv", index=False)

print("======================================================================================================")
df_q22.to_excel('zlfx.xlsx', sheet_name='县区', index=False)
with pd.ExcelWriter('zlfx.xlsx', mode='a', if_sheet_exists='overlay') as writer:
    for area, df in df_q23_result.items():
        df.to_excel(writer, sheet_name=str(area), index=False)
