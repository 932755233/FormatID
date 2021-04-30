

user1 = eval('{"code":"200","data":{"CFBILLSTATUS":"1","CFCUSTOMERID":"0c8AAAAFshO/DAQO","CFCUSTOMERNAME":"（停）昌邑启航兽药有限公司","CFCUSTOMERNUMBER":"2.S.002767","CFPERIODID":"0c8AAAA0eZyCOIxM","CFPERIODNUMBER":"202105","CFSALESMENID":"ovNEpmfBQGOy8DVgahYwJYDvfe0=","CFSALESMENNAME":"薛兴华","FBIZDATE":"2021-04-29","FID":"wR0abvKincLgU88KqMAIojZPhHU=","FNUMBER":"PK2021040013","approveOpinionInfos":[],"attachInfos":[],"fDataCenter":"orcleasdba","saleKpiByMonthEntryInfos":[{"CFASSISTUNITID":"85M4LknST7CwYWrft7IpYFuCXFc=","CFASSISTUNITIDFNUMBER":"124","CFASSISTUNITNAME":"件","CFMATERIALID":"0c8AAABBt/NECefw","CFMATERIALMODEL":"100g*120袋","CFMATERIALNAME":"（S）泰易康 （定制）","CFMATERIALNUMBER":"3.03.N.F.YY.00001","CFQTY":"1","FID":"wR0abvKjncLgU88KqMAIom5qFP0=","FPARENTID":"wR0abvKincLgU88KqMAIojZPhHU="}]},"msg":"成功返回","state":"1"}')
print(user1[0]) # 结果 pengjunlee

for item in user1:
    print(item[0])


