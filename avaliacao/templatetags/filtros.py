from django import template

register = template.Library()

@register.filter
def get_item_at_index(lista, index):
    try:
        return lista[int(index)]
    except (IndexError, ValueError):
        return None
    
@register.filter
def get_verbose_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name

@register.filter
def get_questao(obj,index):
    resposta = getattr(obj,f"questao{index}")
    valor_questoes = ["eliminatorio","eliminatorio","eliminatorio",1,1,2,1,12,2,12,12,3,6,3,3,2,4,2,3,9,3,6,2,2,4,8,16,2,12,9,8,12,8,12,16,12,12,12,6,16,8,8,12,8,12,16,6,6,4,"classificatorio","classificatorio"]
    if resposta == 'AD':
        return {"resposta": "Adequado"}
    elif resposta == "IN":
        return {
            "resposta": "Inadequado",
            "pontuacao": str(valor_questoes[index-1]),
        }
    else:
        return {"resposta": "Não se Aplica"}
@register.filter
def less_than_or_equal(value, arg):
    lower, upper = map(int, arg.split(','))
    return lower <= int(value) <= upper
    
    