from openpyxl.styles import Font
from settings import *
import openpyxl

def format_data(data: str) -> Dict[str, List[str]]:
    try:
        name = data[5]

        service_one = data[1].split(' R$ ')
        service_two = data[2].split(' R$ ')
        service_three = data[3].split(' R$ ')

        item_one = service_one[0] if len(service_one) > 0 else ''
        service_value_one = service_one[2] if len(service_one) > 2 else ''

        item_two = service_two[0] if len(service_two) > 0 else ''
        service_value_two = service_two[2] if len(service_two) > 2 else ''

        item_three = service_three[0] if len(service_three) > 0 else ''
        service_value_three = service_three[2][:3] if len(service_three) > 2 else ''

        due_date = data[19].split(': ')[1] if ': ' in data[19] else data[19]
        tax = data[11].split(': ')[1] if ': ' in data[11] else ''
        total_amount = data[14]
        bank = data[16]
        address = data[22]
        account_number = data[18].split(': ')[1] if ': ' in data[18] else ''
        phone_number = data[23][:-11] if len(data[23]) > 11 else ''
        email_address = data[21] if '@' in data[21] else ''

        formatted_data = [
            name, item_one, service_value_one, item_two, service_value_two,
            item_three, service_value_three, due_date, tax, total_amount,
            bank, address, account_number, phone_number, email_address
        ]

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {'error': True, 'message': str(e), 'data': None}
    
    return{'error': False, 'message': None, 'data': formatted_data}


def save_excel_data(formatted_data: list) -> Dict[str, None]:
    try:
        wb = openpyxl.Workbook()
        ws = wb.active

        headers = ['NOME', 'ITEM 1', 'VALOR 1', 'ITEM 2', 'VALOR 2', 'ITEM 3', 'VALOR 3', 'DATA VENCIMENTO', 'IMPOSTO', 'TOTAL', 'BANCO', 'ENDERECO', 'CONTA', 'TELEFONE', 'EMAIL']
        ws.append(headers)

        for cell in ws[1]:
            cell.font = Font(bold=True)

        formatted_data = format_data(formatted_data)
        
        if formatted_data:
            ws.append(formatted_data['data'])


        file_path = os.path.join(FULL_SPREADSHEETS, f"dados-fatura-{today}.xlsx")

        wb.save(file_path)

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {'error': True, 'message': str(e), 'data': None}
    
    return{'error': False, 'message': None, 'data': None}