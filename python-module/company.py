def _private_name(name: str):
    if name == 'bytedance':
        return 'by*****ce'
    else:
        return '404 not found'

def greeting(company_name: str):
    print(_private_name(company_name))
