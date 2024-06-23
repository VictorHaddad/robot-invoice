from workers import Excel, GetData

def main():
    data_handler = GetData
    excel_handler = Excel  

    data_from_pdf = data_handler.get_values_pdf()
    if data_from_pdf['error']:
        return data_from_pdf

    insert_data_into_excel = excel_handler.save_excel_data(data_from_pdf['data'])
    if insert_data_into_excel['error']:
        return insert_data_into_excel

if __name__ == '__main__':
    main()