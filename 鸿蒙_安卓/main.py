module = '''
   mAllModuleMap = new LinkedHashMap<String, ModuleModel>();
            mAllModuleMap.put(AppConstants.PRIV_PUNCH_CLOCK, new ModuleModel(AppConstants.PRIV_PUNCH_CLOCK, getResources().getString(R.string.main_menu_attendance_statistics), new int[]{R.mipmap.menu_daka, R.mipmap.menu_daka}));
            mAllModuleMap.put(AppConstants.PRIV_ZONGJIEHUIBAO, new ModuleModel(AppConstants.PRIV_ZONGJIEHUIBAO, getResources().getString(R.string.main_menu_huibao), new int[]{R.mipmap.menu_huibao, R.mipmap.menu_huibao}));
            mAllModuleMap.put(AppConstants.PRIV_TIME_TRACKING, new ModuleModel(AppConstants.PRIV_TIME_TRACKING, getResources().getString(R.string.main_menu_chuli), new int[]{R.mipmap.menu_huibaocl, R.mipmap.menu_huibaocl}));
            mAllModuleMap.put(AppConstants.PRIV_PRIV_SALES_MANAGEMENT, new ModuleModel(AppConstants.PRIV_PRIV_SALES_MANAGEMENT, getResources().getString(R.string.main_menu_sale_management), new int[]{R.mipmap.menu_sale, R.mipmap.menu_sale}));
            mAllModuleMap.put(AppConstants.PRIV_ORDER_MANAGEMENT, new ModuleModel(AppConstants.PRIV_ORDER_MANAGEMENT, getResources().getString(R.string.main_menu_order_management), new int[]{R.mipmap.menu_order, R.mipmap.menu_order}));
//            mAllModuleMap.put(AppConstants.PRIV_ACCOUNTS_RECEIVABLE, new ModuleModel(AppConstants.PRIV_ACCOUNTS_RECEIVABLE, getResources().getString(R.string.main_menu_accounts_receivable), new int[]{R.mipmap.menu_yingshoukuan, R.mipmap.menu_yingshoukuan}));
            mAllModuleMap.put(AppConstants.AUTH_REPORT_COST_OFFICE_WORK, new ModuleModel(AppConstants.AUTH_REPORT_COST_OFFICE_WORK, "费用管理(内勤)", new int[]{R.mipmap.menu_cost, R.mipmap.menu_cost}));
            mAllModuleMap.put(AppConstants.PRIV_EXPENSE_MANAGEMENT, new ModuleModel(AppConstants.PRIV_EXPENSE_MANAGEMENT, getResources().getString(R.string.main_menu_cost_management), new int[]{R.mipmap.menu_cost, R.mipmap.menu_cost}));
            mAllModuleMap.put(AppConstants.PRIV_EXPENSE_MANAGEMENT, new ModuleModel(AppConstants.PRIV_EXPENSE_MANAGEMENT, getResources().getString(R.string.main_menu_cost_management), new int[]{R.mipmap.menu_cost, R.mipmap.menu_cost}));

            mAllModuleMap.put(AppConstants.PRIV_CUSTOMER_INDICATORS, new ModuleModel(AppConstants.PRIV_CUSTOMER_INDICATORS, getResources().getString(R.string.main_menu_info_report), new int[]{R.mipmap.menu_kehuzhibiao, R.mipmap.menu_kehuzhibiao}));
//            mAllModuleMap.put(AppConstants.PRIV_TASK_MANAGEMENT, new ModuleModel(AppConstants.PRIV_TASK_MANAGEMENT, getResources().getString(R.string.main_menu_task_management), new int[]{R.mipmap.menu_event, R.mipmap.menu_event}));
            mAllModuleMap.put(AppConstants.PRIV_REPORT_MANAGEMENT, new ModuleModel(AppConstants.PRIV_REPORT_MANAGEMENT, getResources().getString(R.string.main_menu_report_management), new int[]{R.mipmap.menu_report, R.mipmap.menu_report}));
            mAllModuleMap.put(AppConstants.PRIV_CUSTOMS_DOCUMENTATION, new ModuleModel(AppConstants.PRIV_CUSTOMS_DOCUMENTATION, getResources().getString(R.string.main_menu_customs_documentation), new int[]{R.mipmap.menu_kehujiandang, R.mipmap.menu_kehujiandang}));
            mAllModuleMap.put(AppConstants.PRIV_QRCODE_DATA, new ModuleModel(AppConstants.PRIV_QRCODE_DATA, getResources().getString(R.string.main_menu_qrcode_management), new int[]{R.mipmap.menu_qrcode, R.mipmap.menu_qrcode}));
            mAllModuleMap.put(AppConstants.PRIV_ORDER_PROJECT_MANAGEMENT, new ModuleModel(AppConstants.PRIV_ORDER_PROJECT_MANAGEMENT, getResources().getString(R.string.home_col_project_management), new int[]{R.mipmap.menu_project_management, R.mipmap.menu_project_management}));
            mAllModuleMap.put(AppConstants.PRIV_ORDER_KNOWLEDGE_BASE, new ModuleModel(AppConstants.PRIV_ORDER_KNOWLEDGE_BASE, getResources().getString(R.string.home_col_knowledge_base), new int[]{R.mipmap.menu_knowledge_base, R.mipmap.menu_knowledge_base}));
            mAllModuleMap.put(AppConstants.AUTH_REPORT_PRODUCTION_MANAGEMENT, new ModuleModel(AppConstants.AUTH_REPORT_PRODUCTION_MANAGEMENT, getResources().getString(R.string.home_production_management), new int[]{R.mipmap.menu_shengchanguanli, R.mipmap.menu_shengchanguanli}));
            mAllModuleMap.put(AppConstants.AUTH_REPORT_REASONS_NOT_DELIVERING, new ModuleModel(AppConstants.AUTH_REPORT_REASONS_NOT_DELIVERING, getResources().getString(R.string.home_reasons_not_delivering), new int[]{R.mipmap.menu_knowledge_base, R.mipmap.menu_knowledge_base}));
            mAllModuleMap.put(AppConstants.PRIV_CUSTOMER_DATAWAREHOUSE, new ModuleModel(AppConstants.PRIV_CUSTOMER_DATAWAREHOUSE, getResources().getString(R.string.main_menu_management_datawarehouse), new int[]{R.mipmap.menu_report, R.mipmap.menu_report}));
            mAllModuleMap.put(AppConstants.PRIV_CUSTOMER_SALEKPI, new ModuleModel(AppConstants.PRIV_CUSTOMER_SALEKPI, getResources().getString(R.string.main_menu_management_salekpi), new int[]{R.mipmap.menu_kehuzhibiao, R.mipmap.menu_kehuzhibiao}));
            mAllModuleMap.put(AppConstants.PRIV_INVENTORYMATERIAL, new ModuleModel(AppConstants.PRIV_INVENTORYMATERIAL, getResources().getString(R.string.material_info), new int[]{R.mipmap.menu_shengchanguanli, R.mipmap.menu_shengchanguanli}));
//          mAllModuleMap.put(AppConstants.PRIV_FINISHED_PRODUCT, new ModuleModel(AppConstants.PRIV_FINISHED_PRODUCT, getResources().getString(R.string.finished_product_info), new int[]{R.mipmap.menu_shengchanguanli, R.mipmap.menu_shengchanguanli}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_PERMISSIONS, new ModuleModel(AppConstants.PRIV_CENTRE_PERMISSIONS, getResources().getString(R.string.centre_info_list_title), new int[]{R.mipmap.menu_shengchanguanli, R.mipmap.menu_shengchanguanli}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_VIP_CUSTOMERS_LIST, new ModuleModel(AppConstants.PRIV_CENTRE_VIP_CUSTOMERS_LIST, getResources().getString(R.string.vip_customers_manager), new int[]{R.mipmap.menu_kehujiandang, R.mipmap.menu_kehujiandang}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_DAILY_IN_LOG, new ModuleModel(AppConstants.PRIV_CENTRE_DAILY_IN_LOG, getResources().getString(R.string.daily_in_log), new int[]{R.mipmap.menu_daka, R.mipmap.menu_daka}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_DAILY_IN_LOG_DISPOSE, new ModuleModel(AppConstants.PRIV_CENTRE_DAILY_IN_LOG_DISPOSE, getResources().getString(R.string.daily_in_log_dispose), new int[]{R.mipmap.menu_huibaocl, R.mipmap.menu_huibaocl}));
            mAllModuleMap.put(AppConstants.PRIV_STOCKER_CLOCKIN_IN_LOG, new ModuleModel(AppConstants.PRIV_STOCKER_CLOCKIN_IN_LOG, getResources().getString(R.string.daily_tube_in_log), new int[]{R.mipmap.menu_daka, R.mipmap.menu_daka}));
            mAllModuleMap.put(AppConstants.PRIV_STOCKER_CLOCKIN_IN_LOG_DISPOSE, new ModuleModel(AppConstants.PRIV_STOCKER_CLOCKIN_IN_LOG_DISPOSE, getResources().getString(R.string.daily_tube_in_log_dispose), new int[]{R.mipmap.menu_huibaocl, R.mipmap.menu_huibaocl}));
            mAllModuleMap.put(AppConstants.PRIV_MFC_CLOCKIN_NEW, new ModuleModel(AppConstants.PRIV_MFC_CLOCKIN_NEW, getResources().getString(R.string.daily_mfc_clockin_log), new int[]{R.mipmap.menu_daka, R.mipmap.menu_daka}));
            mAllModuleMap.put(AppConstants.PRIV_MFC_CLOCKIN_LIST, new ModuleModel(AppConstants.PRIV_MFC_CLOCKIN_LIST, getResources().getString(R.string.daily_mfc_clockin__dispose), new int[]{R.mipmap.menu_huibaocl, R.mipmap.menu_huibaocl}));
            mAllModuleMap.put(AppConstants.PRIV_QI_CLOCKIN_NEW, new ModuleModel(AppConstants.PRIV_QI_CLOCKIN_NEW, getResources().getString(R.string.daily_qi_clockin_log), new int[]{R.mipmap.menu_daka, R.mipmap.menu_daka}));
            mAllModuleMap.put(AppConstants.PRIV_QI_CLOCKIN_LIST, new ModuleModel(AppConstants.PRIV_QI_CLOCKIN_LIST, getResources().getString(R.string.daily_qi_clockin_dispose), new int[]{R.mipmap.menu_huibaocl, R.mipmap.menu_huibaocl}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_DAILY_PERFOR_MANAGER, new ModuleModel(AppConstants.PRIV_CENTRE_DAILY_PERFOR_MANAGER, getResources().getString(R.string.daily_perfor_manager), new int[]{R.mipmap.menu_neibujixiaoguanl, R.mipmap.menu_neibujixiaoguanl}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_PFM_EXMREQ, new ModuleModel(AppConstants.PRIV_CENTRE_PFM_EXMREQ, getResources().getString(R.string.daily_perfor_manager), new int[]{R.mipmap.menu_shiyanlingyong, R.mipmap.menu_shiyanlingyong}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_TODO_ITEMS, new ModuleModel(AppConstants.PRIV_CENTRE_TODO_ITEMS, getResources().getString(R.string.daily_todo_list), new int[]{R.mipmap.menu_kehuzhibiao, R.mipmap.menu_kehuzhibiao}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_IN_TODO_ITEMS, new ModuleModel(AppConstants.PRIV_CENTRE_IN_TODO_ITEMS, getResources().getString(R.string.daily_in_todo_list), new int[]{R.mipmap.menu_kehuzhibiao, R.mipmap.menu_kehuzhibiao}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_WARRANTY_RELEASE_FORM, new ModuleModel(AppConstants.PRIV_CENTRE_WARRANTY_RELEASE_FORM, getResources().getString(R.string.daily_iwarranty_release_form), new int[]{R.mipmap.menu_zhibao, R.mipmap.menu_zhibao}));
            mAllModuleMap.put(AppConstants.PRIV_WORK_ORDER_LIST, new ModuleModel(AppConstants.PRIV_WORK_ORDER_LIST, getResources().getString(R.string.work_order_title), new int[]{R.mipmap.menu_shebei, R.mipmap.menu_shebei}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_SEMIFINISHED_PRODUCT_INSPECTION, new ModuleModel(AppConstants.PRIV_CENTRE_SEMIFINISHED_PRODUCT_INSPECTION, getResources().getString(R.string.daily_semifinished_product_inspection), new int[]{R.mipmap.menu_project_banchengpzhij, R.mipmap.menu_project_banchengpzhij}));
            mAllModuleMap.put(AppConstants.PRIV_AUTH_MOKA_MANAGE, new ModuleModel(AppConstants.PRIV_AUTH_MOKA_MANAGE, getResources().getString(R.string.home_user_app_text), new int[]{R.mipmap.menu_project_my, R.mipmap.menu_project_my}));
            mAllModuleMap.put(AppConstants.PRIV_CENTRE_EQUIPMENT_REPAIR_BILL, new ModuleModel(AppConstants.PRIV_CENTRE_EQUIPMENT_REPAIR_BILL, getResources().getString(R.string.daily_equipment_repair_bill), new int[]{R.mipmap.menu_shebei, R.mipmap.menu_shebei}));
            mAllModuleMap.put(AppConstants.PRIV_CRAFT_MANAGE, new ModuleModel(AppConstants.PRIV_CRAFT_MANAGE, getResources().getString(R.string.home_craft_manage), new int[]{R.mipmap.menu_daka, R.mipmap.menu_daka}));
            mAllModuleMap.put(AppConstants.PRIV_DETECTION_MANAGE, new ModuleModel(AppConstants.PRIV_DETECTION_MANAGE, getResources().getString(R.string.home_detection_manage), new int[]{R.mipmap.menu_project_banchengpzhij, R.mipmap.menu_project_banchengpzhij}));


'''

if __name__ == '__main__':
    with open('1.txt', 'r', encoding='utf-8') as file:
        index = 0
        for line in file:
            if '{permission' in line:
                lll = line[line.find('\'') + 1:-3] + ",routerUrl:'',count:'',managementIndoor:''},"
                # print(lll)

                permission = line[line.find('\'') + 1:-3]
                permission = permission[0:permission.find('\',')]
                # print(permission)

                title = line[line.find('title:\'') + 7:]
                title = title[:title.find('\'')]

                # print(title)
                index = index + 1
                contentStr = ""
                if "新增"in title:
                    contentStr = '''
          if (userId !== '498') {
              this.dataList.push({
              count: '',
              permission: '%s',
              title: '%s',
              routerUrl: '',
              type: '',
              type_id: '',
              type_style: ''
            })
          }''' % (permission, title)
                else:
                    contentStr = '''
              this.dataList.push({
              count: '',
              permission: '%s',
              title: '%s',
              routerUrl: '',
              type: '',
              type_id: '',
              type_style: ''
            })''' % (permission, title)


                print(contentStr)
    # print(str(index) + "---" + lll)

    with open('1.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if 'public static readonly' in line:
                lll = line[line.find('public'):-1]
                print(lll)
