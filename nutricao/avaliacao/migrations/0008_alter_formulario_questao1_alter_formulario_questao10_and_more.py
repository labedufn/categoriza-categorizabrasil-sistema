# Generated by Django 4.2.16 on 2024-12-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0007_alter_formulario_questao1_alter_formulario_questao10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='questao1',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='1. Utiliza-se exclusivamente água potável para manipulação de alimentos (água de abastecimento público ou solução alternativa com potabilidade atestada semestralmente por meio de laudos laboratoriais)água de abastecimento público ou solução alternativa com potabilidade atestada semestralmente por meio de laudos laboratoriais).'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao10',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='10.Instalações, equipamentos, móveis e utensílios mantidos em condições higiênico-sanitárias apropriadas.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao11',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='11.Frequência adequada de higienização dos equipamentos, móveis e utensílios.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao12',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='12.Utensílios utilizados na higienização de instalações distintos daqueles usados para higienização das partes dos equipamentos e utensílios que entrem em contato com o alimento.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao13',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='13.Diluição, tempo de contato e modo de uso ou aplicação dos produtos saneantes obedece às instruções recomendadas pelo fabricante.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao14',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='14.Produtos saneantes regularizados pelo Ministério da Saúde.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao15',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='15. Áreas de preparação higienizadas quantas vezes forem necessárias e imediatamente após o término do trabalho.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao16',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='16.Controle de vetores e pragas urbanas executados por empresa especializada devidamente regularizada'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao17',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='17. Existência de um conjunto de ações eficazes e contínuas com o objetivo de impedir a atração, o abrigo, o acesso e ou proliferação de vetores e pragas urbanas.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao18',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='18.Edificações, instalações, equipamentos, móveis e utensílios livres da presença de animais, incluindo vetores e pragas urbanas.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao19',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='19. Os manipuladores são afastados da preparação de alimentos quando apresentam lesões e ou sintomas de enfermidades.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao2',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='2.  Instalações abastecidas de água corrente.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao20',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='20. Lavam cuidadosamente as mãos ao chegar ao trabalho, antes e após manipular o alimento, após qualquer interrupção do serviço, após tocar materiais contaminados, após usar os sanitários e sempre que se fizer necessário.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao21',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='21.Não fumam e falam quando desnecessário, cantam, assobiam, espirram, cospem, tossem, comem, manipulam dinheiro ou praticam outros atos que possam contaminar o alimento durante o desempenho das atividades.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao22',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='22.Submetidos à inspeção e aprovação na recepção.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao23',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='23.Matérias-primas, ingredientes e embalagens utilizados para preparação em condições higiênico sanitárias adequadas.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao24',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='24.Embalagens primárias das matérias-primas e dos ingredientes íntegras.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao25',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='25.Utilização das matérias primas e ingredientes respeita o prazo de validade ou se observa a ordem de entrada.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao26',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='26.Matérias-primas fracionadas adequadamente acondicionadas e identificadas com, no mínimo, as seguintes informações: designação do produto, data de fracionamento e prazo de validade após abertura ou retirada da embalagem original.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao27',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='27.Temperatura das matérias-primas e ingredientes perecíveis verificada na recepção e no armazenamento.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao28',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='28. Gelo utilizado em alimentos fabricado a partir de água potável e mantido em condição higiênico sanitária.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao29',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='29.Lavatórios da área de preparação dotados dos produtos destinados à higiene das mãos (sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e produto antisséptico, toalhas de papel não reciclado ou outro sistema higiênico e seguro de secagem das mãos),sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e produto antisséptico, toalhas de papel não reciclado ou outro sistema higiênico e seguro de secagem das mãos).'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao3',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='3. Instalações dispõem de conexões com rede de esgoto ou fossa séptica.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao30',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='30.Durante o preparo, aqueles que manipulam alimentos crus realizam a lavagem e a antissepsia das mãos antes de manusear alimentos preparados.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao31',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='31.Produtos perecíveis expostos à temperatura ambiente somente pelo tempo mínimo necessário para preparação do alimento.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao32',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='32. Descongelamento conduzido conforme orientação do fabricante e utilizando uma das seguintes técnicas: refrigeração à temperatura inferior a 5ºC ou em forno de micro-ondas quando o alimento for submetido imediatamente à cocção.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao33',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='33.Alimentos submetidos ao descongelamento mantidos sob refrigeração se não forem imediatamente utilizados e não se recongela.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao34',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='34.Tratamento térmico garante que todas as partes do alimento atinjam a temperatura de, no mínimo, 70ºC, ou outra combinação de tempo e temperatura desde que assegure a qualidade higiênico-sanitária dos alimentos.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao35',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='35.Avalia-se a eficácia do tratamento térmico.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao36',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='36.Temperatura do alimento preparado no resfriamento reduzida de 60ºC a 10ºC em até 2 horas.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao37',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='37.Após o resfriamento, alimento preparado conservado sob refrigeração a temperaturas inferiores a 5ºC, ou congelado à temperatura igual ou inferior a - 18ºC.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao38',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='38.Alimentos consumidos crus, quando aplicável, submetidos a processo de higienização com produtos regularizados e aplicados de forma a evitar a presença de resíduos.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao39',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='39.Evita-se o contato direto ou indireto entre alimentos crus, semi-prontos e prontos para o consumo.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao4',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='4.Reservatório devidamente tampado e conservado (livre de rachaduras, vazamentos, infiltrações, descascamentos, dentre outros defeitos),livre de rachaduras, vazamentos, infiltrações, descascamentos, dentre outros defeitos).'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao40',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='40.Possuem termômetro comprovadamente calibrado para a aferição da temperatura dos alimentos.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao41',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='41.Alimento preparado armazenado sob refrigeração ou congelamento identificado com no mínimo as seguintes informações: designação, data de preparo e prazo de validade.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao42',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='42.Prazo máximo de consumo do alimento preparado e conservado sob refrigeração é de 5 dias, caso a temperatura de conservação seja igual ou inferior a 4ºC. Quando forem utilizadas temperaturas superiores a 4°C e inferiores a 5°C, o prazo máximo de consumo é reduzido.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao43',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='43.Alimento preparado e conservado sob refrigeração mantido à temperatura igual a 5ºC ou inferior.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao44',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='44.Alimentos conservados a quente mantidos a temperatura superior a 60ºC e o tempo ao longo da cadeia de preparo até exposição não excede a 6 horas.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao45',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='45.Alimentos preparados mantidos à temperatura superior a 60ºC.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao46',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='46.Temperatura dos equipamentos de exposição regularmente monitorada..'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao47',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='47.Na exposição, manipuladores adotam procedimentos que minimizem o risco de contaminação dos alimentos preparados, por meio da antissepsia das mãos e pelo uso de utensílios ou luvas descartáveis (quando aplicável),quando aplicável).'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao48',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='48. Alimentos preparados, mantidos na área de armazenamento ou aguardando o transporte, identificados (designação do produto, data de preparo e o prazo de validade) e protegidos contra contaminantes,designação do produto, data de preparo e o prazo de validade) e protegidos contra contaminantes.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao49',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='49.Armazenamento e transporte ocorrem em condições de tempo e temperatura que não comprometam a qualidade higiênico-sanitária do alimento preparado.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao5',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='5. Reservatório em adequado estado de higiene.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao50',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='50.Possui um responsável pelas atividades de manipulação de alimentos (responsável técnico, proprietário ou funcionário designado) comprovadamente capacitado.responsável técnico, proprietário ou funcionário designado) comprovadamente capacitado. '),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao51',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='51.Possui implementado o Manual de Boas Práticas e os Procedimentos Operacionais Padronizados'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao6',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='6. Reservatório de água higienizado em intervalo máximo de seis meses, sendo mantidos registros da operação.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao7',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='7. Material que reveste internamente o reservatório de água não compromete a qualidade da água.'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao8',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='8. Instalações sanitárias possuem lavatórios de mãos e os produtos destinados à higiene pessoal (papel higiênico, sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e antisséptico, coletores com tampa e acionados sem contato manual e toalhas de papel não reciclado ou outro sistema higiênico e seguro para secagem das mãos),papel higiênico, sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e antisséptico, coletores com tampa e acionados sem contato manual e toalhas de papel não reciclado ou outro sistema higiênico e seguro para secagem das mãos).'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='questao9',
            field=models.CharField(blank=True, choices=[('AD', 'Adequado'), ('IN', 'Inadequado'), ('NA', 'Não se Aplica')], max_length=10, verbose_name='9.Existe separação entre as diferentes atividades por meios físicos ou por outros meios eficazes de forma a evitar a contaminação cruzada.'),
        ),
    ]
