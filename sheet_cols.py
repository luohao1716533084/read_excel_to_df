#coding:utf-8

# 输出表说明:
import os

"""
n值说明:
case1:当表类型为A时,需要删除的行数等于n;
case2:当表类型为B时,且为标准表时,n等于0;
case3:当表类型为B是,且首行(列名)与数据行有n行的间隔时,n等于n+1;
"""

"""
根据网管导出的历史性能_切换入切换对指标_邻区对_KM_20230209104349_1.xls,提取临时邻区对。
临时邻区定义:
a.请求次数不为0(系统内每相邻关系切换出请求次数);
b.请求执行次数不为0(系统内每相邻关系切换出执行请求次数);
typeA
"""


ncell_pair_on_5g_dict = {
    'excelName': '邻区漏配核查',
    'sheetName': 'Sheet0',
    'cols': ['eNodeBId', 'LocalCellId', 'E-UTRAN FDD小区名称', 'Mcc', 'Mnc', 'AccessId',  'PeerCellId', '系统内每相邻关系切换出请求次数', '系统内每相邻关系切换出执行请求次数', '邻区漏配(小区对)'],
    'colsAlias': ['网元', '小区', '小区名称', 'nbrMCC', 'nbrMNC', 'nbrEnbId', 'nbrCellId', '请求次数', '执行次数', '邻区漏配对'],
    'n': 0,
    'flag': 'B',
    'index': False
}
    
ncell_pair_dict = {
    'excelName': 'yn_zxgs_ncell_pair',
    'cols': ['网元', '小区', '小区名称', '邻区关系', '系统内每相邻关系切换出请求次数', '系统内每相邻关系切换出执行请求次数', '邻区漏配(小区对)'],
    'colsAlias': ['网元', '小区', '小区名称', '邻区关系', '请求次数', '执行次数', '邻区漏配对'],
    'n': 0,
    'index': False
}

"""
根据网管导出的历史性能_邻区漏配提取漏配邻区对。
typeB
"""
lack_NcellPair_dict = {
    'excelName': '历史性能_邻区漏配',
    'sheetName': 'sheet1',
    'cols': ['网元', '小区', '小区名称', '邻区关系', '邻区漏配(小区对)'],
    'n': 0,
    'flag': 'B',
    'index': True
}

#工参表
gongcan_dx_4G_dict = {
    'excelName': '昆明电信基础信息4G工参-1204(新场景归类)',
    'sheetName': 'rnohelper',
    'cols': ['基站ID', '小区标识', 'enodeNameEn（英文基站名）', '小区名(英文小区名)', 
             '频段', '经度', '纬度', '城市边界（主城区，县城，乡镇，行政村自然村）', '上行链路的中心载频(MHz)', '下行链路的中心载频(MHz)',
             'PCI', 'TAC', '小区上行系统频域带宽(Hz)', '小区下行系统频域带宽(Hz)'],
    'colsAlias': ['网元', '小区', 'enodeName', '小区名称', 
                  'freqBandInd', 'lon', 'lat', '城市边界', 'earfcnUl', 'earfcnDl', 
                  'pci', 'tac',  'bandWidthUl', 'bandWidthDl'],
    'n': 0,
    'flag': 'B',
    'index': False
}

#工参表
gongcan_lt_4G_dict = {
    'excelName': '昆明联通LTE',
    'sheetName': 'Sheet1',
    'cols': ['eNbID', '小区标识', 'eNbName', 'CellName',
             'Freq', 'Longitude', 'Latitude', '乡镇',
             'PCI', 'TAC', '小区带宽'],
    'colsAlias': ['网元', '小区', 'enodeName', '小区名称',
                  'Freq', 'lon', 'lat', '城市边界',
                  'pci', 'tac',  'bandWidthUl'],
    'n': 0,
    'flag': 'B',
    'index': False
}



exitSite_dict = {
    'excelName': '昆明电信基础信息4G工参-1204(新场景归类)',
    'sheetName': '退网小区',
    'cols': ['基站ID', '小区号'],
    'colsAlias': ['网元', '小区'],
    'n': 0,
    'flag': 'B',
    'index': False
}

# 黑名单列表 old
# black_list_dict = {
#     'excelName': 'NBRBlackLstFDD',
#     'sheetName': 'Son Black Nbr Cell Query',
#     'cols': ['MEID', 'srvCellId', 'nbrEnbId', 'nbrCellId', 'nbrMCC', 'nbrMNC'],
#     'colsAlias': ['网元', '小区',  'nbrEnbId', 'nbrCellId', 'nbrMCC', 'nbrMNC'],
#     'n': 3,
#     'flag': 'B',
#     'index': False
# }

# 黑名单列表 new
black_list_dict_son = {
    'excelName': 'Son Black Nbr Cell Query Result',
    'sheetName': 'Son Black Nbr Cell Query',
    'cols': ['源网元ID', '源小区ID', '源小区ECGI', '目标小区ECGI', '邻区类型（0：临时；1：正式）'],
    'colsAlias': ['网元', '小区',  'ECI', '邻区关系', '邻区类型'],
    'n': 1,
    'index': False
}


# 黑名单列表 new
black_list_dict_sonm = {
    'excelName': 'BlackListofNeighborCellManagement',
    'sheetName': 'BlackListofNeighbor',
    'cols': ['源端基站标识', '源端小区标识', '邻接小区PLMN', '邻接基站标识', '邻接小区标识', '邻区类型'],
    'colsAlias': ['网元', '小区',  '邻接小区PLMN', '邻接基站id', '邻接小区id', '邻区类型'],
    'n': 0,
    'index': False
}



# 邻区关系
EUtranRelation_4g_dict = {
    'excelName': 'CM_PLAN_FDD_RADIO',
    'sheetName': 'EUtranRelation',
    'cols': ['MEID', 'CellId', 'mcc', 'mnc', 'eNBId', 'NCellId'],
    'colsAlias': ['网元', '小区', 'nbrMCC', 'nbrMNC', 'nbrEnbId', 'nbrCellId'],
    'n': 4,
    'flag': 'B',
    'index': True
}

# 外部小区
ExternalEUtranCellFDD_4g_dict = {
    'excelName': 'CM_PLAN_FDD_RADIO',
    'sheetName': 'ExternalEUtranCellFDD',
    'cols': ['srcENBId', 'mcc', 'mnc', 'eNBId', 'cellLocalId', 'freqBandInd', 'earfcnUl', 'earfcnDl', 'pci', 'tac', 'bandWidthUl', 'bandWidthDl'],
    'colsAlias': ['网元', 'nbrMCC', 'nbrMNC', 'nbrEnbId', 'nbrCellId', 'freqBandInd', 'earfcnUl', 'earfcnDl', 'pci', 'tac', 'bandWidthUl', 'bandWidthDl'],
    'n': 4,
    'flag': 'B',
    'index': False
}



#  5g网管上，外部小区
ExternalEUtranCellFDD_5g_dict = {
    'excelName': 'adjustneighborcell',
    'sheetName': 'ExternalEUtranCellFDDLTE',
    'cols': ['ENBCUCPFunction_moId', 'mcc', 'mnc', 'eNBId', 'CellId', 'freqBandInd', 'earfcnUl', 'earfcnDl', 'pci', 'tac', 'bandWidthUl', 'bandWidthDl'],
    'colsAlias': ['网元', 'nbrMCC', 'nbrMNC', 'nbrEnbId', 'nbrCellId', 'freqBandInd', 'earfcnUl', 'earfcnDl', 'pci', 'tac', 'bandWidthUl', 'bandWidthDl'],
    'n': 4,
    'flag': 'B',
    'index': False
}

#  5g网管上，邻区关系
EUtranRelation_5g_dict = {
    'excelName': 'adjustneighborcell',
    'sheetName': 'EUtranRelationFDDLTE',
    'cols': ['sourceEnbId', 'CellId', 'mcc', 'mnc', 'targetEnbId', 'targetCellId'],
    'colsAlias': ['网元', '小区', 'nbrMCC', 'nbrMNC', 'nbrEnbId', 'nbrCellId'],
    'n': 4,
    'flag': 'B',
    'index': False
}


bandWithDict = {0:1.4, 1:3, 2:5, 3:10, 4:15, 5:20, 6:8, 7:16, 8:4.4, 9:2.4, 10:2.6, 11:2.8, 12:4.6,
                13:4.8, 14:7.2, 15:7.4, 16:7.6, 17:7.8, 18:8.2, 19:8.4, 20:8.6, 21:8.8, 22:9, 23:9.2,
                24:13.2, 25:13.6, 26:14, 27:17.4, 28:17.8, 29:18.2, 30:18.6, 31:7.5, 32:14.8}



res_lackNcellcols = ['index', '网元', '小区', '小区名称', '邻区关系', '邻区漏配(小区对)', "系统内每相邻关系切换出请求次数", "系统内每相邻关系切换出执行请求次数",
                     '是否为临时邻区', '是否为黑名单', '城市边界', '距离(km)']
res_relationNcell = ['网元', '小区', 'nbrMCC', 'nbrMNC', 'nbrEnbId', 'nbrCellId', '邻区关系', 'ECI_x', '是否为黑名单', '城市边界', '距离(km)']

checkColNamesList = ['ECI', 'freqBandInd', 'earfcnUl', 'earfcnDl', 'pci', 'tac', 'bandWidthUl', 'bandWidthDl']
colsName = ['ECI_nbr', 'freqBandInd_nbr', 'earfcnUl_nbr', 'earfcnDl_nbr', 'pci_nbr', 'tac_nbr', 'bandWidthUl_nbr', 'bandWidthDl_nbr']
colsNameSrc = ['freqBandInd', 'earfcnUl', 'earfcnDl', 'pci', 'tac', 'bandWidthUl', 'bandWidthDl']