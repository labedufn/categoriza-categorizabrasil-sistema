from django import forms
from django.db import models

from .models import Formulario

class CustomRadioSelect(forms.RadioSelect):
        template_name = 'custom_radio.html'

class FormularioAvaliacao(forms.ModelForm):

    pode_gerar_relatorio = False
    valor_questoes = ["eliminatorio","eliminatorio","eliminatorio",1,1,2,1,12,2,12,12,3,6,3,3,2,4,2,3,9,3,6,2,2,4,8,16,2,12,9,8,12,8,12,16,12,12,12,6,16,8,8,12,8,12,16,6,6,4,"classificatorio","classificatorio"]
    lista_requisitos = [
    "1. Utiliza-se exclusivamente água potável para manipulação de alimentos (água de abastecimento público ou solução alternativa com potabilidade atestada semestralmente por meio de laudos laboratoriais).",
    "2. Instalações abastecidas de água corrente.",
    "3. Instalações dispõem de conexões com rede de esgoto ou fossa séptica.",
    "4. Reservatório devidamente tampado e conservado (livre de rachaduras, vazamentos, infiltrações, descascamentos, dentre outros defeitos).",
    "5. Reservatório em adequado estado de higiene.",
    "6. Reservatório de água higienizado em intervalo máximo de seis meses, sendo mantidos registros da operação.",
    "7. Material que reveste internamente o reservatório de água não compromete a qualidade da água.",
    "8. Instalações sanitárias possuem lavatórios de mãos e os produtos destinados à higiene pessoal (papel higiênico, sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e antisséptico, coletores com tampa e acionados sem contato manual e toalhas de papel não reciclado ou outro sistema higiênico e seguro para secagem das mãos).",
    "9. Existe separação entre as diferentes atividades por meios físicos ou por outros meios eficazes de forma a evitar a contaminação cruzada.",
    "10. Instalações, equipamentos, móveis e utensílios mantidos em condições higiênico-sanitárias apropriadas.",
    "11. Frequência adequada de higienização dos equipamentos, móveis e utensílios.",
    "12. Utensílios utilizados na higienização de instalações distintos daqueles usados para higienização das partes dos equipamentos e utensílios que entrem em contato com o alimento.",
    "13. Diluição, tempo de contato e modo de uso ou aplicação dos produtos saneantes obedece às instruções recomendadas pelo fabricante.",
    "14. Produtos saneantes regularizados pelo Ministério da Saúde.",
    "15. Áreas de preparação higienizadas quantas vezes forem necessárias e imediatamente após o término do trabalho.",
    "16. Controle de vetores e pragas urbanas executados por empresa especializada devidamente regularizada.",
    "17. Existência de um conjunto de ações eficazes e contínuas com o objetivo de impedir a atração, o abrigo, o acesso e ou proliferação de vetores e pragas urbanas.",
    "18. Edificações, instalações, equipamentos, móveis e utensílios livres da presença de animais, incluindo vetores e pragas urbanas.",
    "19. Os manipuladores são afastados da preparação de alimentos quando apresentam lesões e ou sintomas de enfermidades.",
    "20. Lavam cuidadosamente as mãos ao chegar ao trabalho, antes e após manipular o alimento, após qualquer interrupção do serviço, após tocar materiais contaminados, após usar os sanitários e sempre que se fizer necessário.",
    "21. Não fumam e falam quando desnecessário, cantam, assobiam, espirram, cospem, tossem, comem, manipulam dinheiro ou praticam outros atos que possam contaminar o alimento durante o desempenho das atividades.",
    "22. Submetidos à inspeção e aprovação na recepção.",
    "23. Matérias-primas, ingredientes e embalagens utilizados para preparação em condições higiênico sanitárias adequadas.",
    "24. Embalagens primárias das matérias-primas e dos ingredientes íntegras.",
    "25. Utilização das matérias primas e ingredientes respeita o prazo de validade ou se observa a ordem de entrada.",
    "26. Matérias-primas fracionadas adequadamente acondicionadas e identificadas com, no mínimo, as seguintes informações: designação do produto, data de fracionamento e prazo de validade após abertura ou retirada da embalagem original.",
    "27. Temperatura das matérias-primas e ingredientes perecíveis verificada na recepção e no armazenamento.",
    "28. Gelo utilizado em alimentos fabricado a partir de água potável e mantido em condição higiênico sanitária.",
    "29. Lavatórios da área de preparação dotados dos produtos destinados à higiene das mãos (sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e produto antisséptico, toalhas de papel não reciclado ou outro sistema higiênico e seguro de secagem das mãos).",
    "30. Durante o preparo, aqueles que manipulam alimentos crus realizam a lavagem e a antissepsia das mãos antes de manusear alimentos preparados.",
    "31. Produtos perecíveis expostos à temperatura ambiente somente pelo tempo mínimo necessário para preparação do alimento.",
    "32. Descongelamento conduzido conforme orientação do fabricante e utilizando uma das seguintes técnicas: refrigeração à temperatura inferior a 5ºC ou em forno de micro-ondas quando o alimento for submetido imediatamente à cocção.",
    "33. Alimentos submetidos ao descongelamento mantidos sob refrigeração se não forem imediatamente utilizados e não se recongela.",
    "34. Tratamento térmico garante que todas as partes do alimento atinjam a temperatura de, no mínimo, 70ºC, ou outra combinação de tempo e temperatura desde que assegure a qualidade higiênico-sanitária dos alimentos.",
    "35. Avalia-se a eficácia do tratamento térmico.",
    "36. Temperatura do alimento preparado no resfriamento reduzida de 60ºC a 10ºC em até 2 horas.",
    "37. Após o resfriamento, alimento preparado conservado sob refrigeração a temperaturas inferiores a 5ºC, ou congelado à temperatura igual ou inferior a - 18ºC.",
    "38. Alimentos consumidos crus, quando aplicável, submetidos a processo de higienização com produtos regularizados e aplicados de forma a evitar a presença de resíduos.",
    "39. Evita-se o contato direto ou indireto entre alimentos crus, semi-prontos e prontos para o consumo.",
    "40. Possuem termômetro comprovadamente calibrado para a aferição da temperatura dos alimentos.",
    "41. Alimento preparado armazenado sob refrigeração ou congelamento identificado com no mínimo as seguintes informações: designação, data de preparo e prazo de validade.",
    "42. Prazo máximo de consumo do alimento preparado e conservado sob refrigeração é de 5 dias, caso a temperatura de conservação seja igual ou inferior a 4ºC. Quando forem utilizadas temperaturas superiores a 4°C e inferiores a 5°C, o prazo máximo de consumo é reduzido.",
    "43. Alimento preparado e conservado sob refrigeração mantido à temperatura igual a 5ºC ou inferior.",
    "44. Alimentos conservados a quente mantidos a temperatura superior a 60ºC e o tempo ao longo da cadeia de preparo até exposição não excede a 6 horas.",
    "45. Alimentos preparados mantidos à temperatura superior a 60ºC.",
    "46. Temperatura dos equipamentos de exposição regularmente monitorada.",
    "47. Na exposição, manipuladores adotam procedimentos que minimizem o risco de contaminação dos alimentos preparados, por meio da antissepsia das mãos e pelo uso de utensílios ou luvas descartáveis (quando aplicável).",
    "48. Alimentos preparados, mantidos na área de armazenamento ou aguardando o transporte, identificados (designação do produto, data de preparo e o prazo de validade) e protegidos contra contaminantes.",
    "49. Armazenamento e transporte ocorrem em condições de tempo e temperatura que não comprometam a qualidade higiênico-sanitária do alimento preparado.",
    "50. Possui um responsável pelas atividades de manipulação de alimentos (responsável técnico, proprietário ou funcionário designado) comprovadamente capacitado.",
    "51 Possui implementado o Manual de Boas Práticas e os Procedimentos Operacionais Padronizados."
    ]
    class Meta:
        model = Formulario
        fields = ['questao1','questao1_descricao', 'questao2','questao2_descricao'
                  ,'questao3','questao3_descricao', 'questao4','questao4_descricao',
                  'questao5','questao5_descricao', 'questao6','questao6_descricao',
                  'questao7', 'questao7_descricao','questao8','questao8_descricao',
                  'questao9','questao9_descricao', 'questao10','questao10_descricao',
                  'questao11', 'questao11_descricao','questao12','questao12_descricao',
                  'questao13','questao13_descricao','questao14', 'questao14_descricao',
                  'questao15','questao15_descricao','questao16','questao16_descricao',
                  'questao17','questao17_descricao', 'questao18','questao18_descricao'
                  ,'questao19','questao19_descricao', 'questao20','questao20_descricao',
                  'questao21','questao21_descricao', 'questao22','questao22_descricao',
                  'questao23', 'questao23_descricao','questao24','questao24_descricao',
                  'questao25','questao25_descricao', 'questao26','questao26_descricao',
                  'questao27', 'questao27_descricao','questao28','questao28_descricao',
                  'questao29','questao29_descricao','questao30', 'questao30_descricao',
                  'questao31','questao31_descricao','questao32','questao32_descricao',
                  'questao33','questao33_descricao', 'questao34','questao34_descricao'
                  ,'questao35','questao35_descricao', 'questao36','questao36_descricao',
                  'questao37','questao37_descricao', 'questao38','questao38_descricao',
                  'questao39', 'questao39_descricao','questao40','questao40_descricao',
                  'questao41','questao41_descricao', 'questao42','questao42_descricao',
                  'questao43', 'questao43_descricao','questao44','questao44_descricao',
                  'questao45','questao45_descricao','questao46', 'questao46_descricao',
                  'questao47','questao47_descricao','questao48','questao48_descricao',
                  'questao49', 'questao49_descricao','questao50','questao50_descricao',
                  'questao51','questao51_descricao',
                  ]
        

   