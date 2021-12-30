

import requests
import json


def currency(orderby=None, filter=None, skip=None, top=None):
    """
    Provides the list of currencies for which this data set is available.
     Args:
        orderby(str)[Optional]: Entity properties order selection. e.g. Name asc, Age desc.
        filter (str)[Optional]: Entities filter selection. e.g. Name eq ‘John’
        skip   (str)[Optional]: Index (greater than or equal to zero) of the first entity that will be returned
        top    (str)[Optional]: Maximum number (greater than zero) of entities that will be returned
    Returns:
        object: Show Symbol,CurrencyName,CurrencyType.
    """
    url = "https://olinda.bcb.gov.br/olinda/service/PTAX/version/v1/odata/Currencies?$top=100&$format=json"

    response = requests.get(url)
    fields = response.content.decode('utf8').replace("'", '"')
    data = json.loads(fields)

    return {
        "symbol": data['value'][0]['simbolo'],
        "CurrencyName": data['value'][0]['nomeFormatado'],
        "CurrencyType": data['value'][0]['tipoMoeda']
    }


def exchange_date_rate(currency, date, orderby=None, filter=None, skip=None, top=None):
    """
    Provides bid and offer parities, bid and offer rates for the requested date. There are 5 bulletins daily.
    Args:
        currrency (str)         : 3 letter symbol e.g 'USD'
        date (str)              : format 'MM-DD-YYYY'
        orderby (str) [Optional]: Entity properties order selection. e.g. Name asc, Age desc
        filter (str) [Optional] : Entities filter selection. e.g. Name eq ‘John’
        skip (str) [Optional]   : Index (greater than or equal to zero) of the first entity that will be returned
        top (str)[Optional]     : Maximum number (greater than zero) of entities that will be returned
    Returns:
        list: Provides bid and offer parities, bid and offer rates for the requested date. There are 5 bulletins daily.
    """
    l = []
    url = "https://olinda.bcb.gov.br/olinda/service/PTAX/version/v1/odata/ExchangeRateDate(moeda=@moeda,dataCotacao=@dataCotacao)?%40moeda='{}'&%40dataCotacao='{}'&%24format=json".format(
        currency, date)
    if(orderby):
        url += "&%24orderby="+orderby
    if(filter):
        url += "&%24filter ="+filter
    if(skip):
        url += "&%24filter="+str(skip)
    if(top):
        url += "&%24top="+str(top)
    res = requests.get(url)
    dd = res.content.decode('utf8').replace("'", '"')
    data = json.loads(dd)
    for i in data['value']:
        d = {
            'bidparity': i['paridadeCompra'],
            'offerparity': i['paridadeVenda'],
            'bidrate': i['cotacaoCompra'],
            'offerrate': i['cotacaoVenda'],
            'datetime': i['dataHoraCotacao'],
            'bulletintime': i['tipoBoletim'],
        }
        l.append(d)
    return l


def exchange_rate_period(currency, start_date, end_date, orderby=None, filter=None, skip=None, top=None):
    """
    Provides bid and offer parities, bid and offer rates for the requested time period. There are 5 bulletins daily.
     Args:
        currency (str)          : 3 letter symbol e.g 'USD'
        start_date (str)        : format 'MM-DD-YYYY'
        end_date (str)          : format 'MM-DD-YYYY'
        orderby (str) [Optional]: Entity properties order selection. e.g. Name asc, Age desc
        filter (str) [Optional] : Entities filter selection. e.g. Name eq ‘John’
        skip (int) [Optional]   : Index (greater than or equal to zero) of the first entity that will be returned
        top (int )[Optional]    : Maximum number (greater than zero) of entities that will be returned

    Returns:
        bool: The return value. True for success, False otherwise.
    """

    url = "https://olinda.bcb.gov.br/olinda/service/PTAX/version/v1/odata/ExchangeRatePeriod(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='{}'&@dataInicial='{}'&@dataFinalCotacao='{}'&$top=100&$format=json".format(
        currency, start_date, end_date)

    list = []
    if (orderby):
        url += "&%24orderby="+orderby
    if(filter):
        url += "&%24filter ="+filter
    if(skip):
        url += "&%24filter="+str(skip)
    if(top):
        url += "&%24top="+str(top)

    response = requests.get(url)
    dd = response.content.decode('utf8').replace("'", '"')
    data = json.loads(dd)

    for i in data['value']:
        fields = {
            'BidParity': i['paridadeCompra'],
            'OfferParity': i['paridadeVenda'],
            'BidRate': i['cotacaoCompra'],
            'OfferRate': i['cotacaoVenda'],
            'DateTime': i['dataHoraCotacao'],
            'BulletinTime': i['tipoBoletim'],
        }
        list.append(fields)
    return list


def dollar_rate_date(date, orderby=None, filter=None, skip=None, top=None):
    """
    Provides bid and offer rates for the requested date.
     Args:
        date (str)              : format 'MM-DD-YYYY'
        orderby (str) [Optional]: Entity properties order selection. e.g. Name asc, Age desc
        filter (str) [Optional] : Entities filter selection. e.g. Name eq ‘John’
        skip (int) [Optional]   : Index (greater than or equal to zero) of the first entity that will be returned
        top (int) [Optional]    : Maximum number (greater than zero) of entities that will be returned

    Returns:
        object: bid and offer rates for the requested date.
    """
    url = "https://olinda.bcb.gov.br/olinda/service/PTAX/version/v1/odata/DollarRateDate(dataCotacao=@dataCotacao)?%40dataCotacao='{}'&%24format=json".format(
        date)
    if(orderby):
        url += "&%24orderby="+orderby
    if(filter):
        url += "&%24filter ="+filter
    if(skip):
        url += "&%24filter="+str(skip)
    if(top):
        url += "&%24top="+str(top)
    res = requests.get(url)
    dd = res.content.decode('utf8').replace("'", '"')
    data = json.loads(dd)
    # return data['value']
    return {
        "Bidrate": data['value'][0]['cotacaoCompra'],
        "Offerrate": data['value'][0]['cotacaoVenda'],
        "Datetime": data['value'][0]['dataHoraCotacao']
    }


def dollar_rate_period(start_date, end_date, orderby=None, filter=None, skip=None, top=None):
    """
    Provides bid and offer rates for the requested time period.
     Args:
        currency (str): 3 letter symbol e.g 'USD'
        start_date (str): format 'MM-DD-YYYY'
        end_date (str): format 'MM-DD-YYYY'
        orderby (str) [Optional] : Entity properties order selection. e.g. Name asc, Age desc
        filter (str) [Optional] : Entities filter selection. e.g. Name eq ‘John’
        skip (int) [Optional] : Index (greater than or equal to zero) of the first entity that will be returned
        top (int) [Optional] : Maximum number (greater than zero) of entities that will be returned

    Returns:
        object: Provides bid and offer rates for the requested date
    """

    url = "https://olinda.bcb.gov.br/olinda/service/PTAX/version/v1/odata/DollarRatePeriod(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=''&@dataFinalCotacao=''&$top=100&$format=json".format(
        start_date, end_date)

    if (orderby):
        url += "&%24orderby="+orderby
    if (filter):
        url += "&%24filter ="+filter
    if(skip):
        url += "&%24filter="+str(skip)
    if(top):
        url += "&%24top="+str(top)

    response = requests.get(url)
    dd = response.content.decode('utf8').replace("'", '"')
    data = json.loads(dd)

    return {
        "BidRate": data['value'][0]['cotacaoCompra'],
        "OfferRate": data['value'][0]['cotacaoVenda'],
        "DateTime": data['value'][0]['dataHoraCotacao']
    }
