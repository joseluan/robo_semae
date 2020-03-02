import unittest
from SEMAE import SEMAE

class TestExtractMethods(unittest.TestCase):
    def teste_0_getPageHtml(self):        
        semae = SEMAE()
        self.assertEqual(semae.getTitlePage(803), 'Moradores do Santa Teresa participam da prestação da contas do Semae')

    def teste_1_getPageHtml(self):
        html = '''<!DOCTYPE HTML>\r\n<html lang="pt-br">\r\n\t<head>\r\n\t\t<meta charset="UTF-8">\r\n\t\t<title>SEMAE Serviço Municipal de Água e Esgotos de São Leopoldo - RS</title>\r\n        \r\n        <meta name="keywords" content="semae rs, São Leopoldo, Serviço Municiapl de Água e Esgotos, Ciclo da àgua, Direitos da água, projetos ambientais, assemae, prefeitura de são leopoldo, w3chost, rio grande do sul, comitesinos, conta de água, visite o semae, semae centro, semae zona leste, semase zona norte, semae zona oeste, eta, feitura, scharlau, vicentina, pinheiros, tratamento da água" />\r\n        \r\n\t<meta name="description" content="O Semae é responsável pela gestão dos serviços de captação, adução, produção, tratamento e distribuição de água potável, bem como a coleta, afastamento, tratamento e disposição final dos esgotos, além das operações de micro e macrodrenagem."    \r\n    \r\n    <meta name="DC.identifier" scheme="DCTERMS.URI" content="http://www.semae.rs.gov.br" /><!-- Colocar URL do site -->\r\n    \r\n\t<meta name="DC.subject" lang="pt" content="O Semae é responsável pela gestão dos serviços de captação, adução, produção, tratamento e distribuição de água potável, bem como a coleta, afastamento, tratamento e disposição final dos esgotos, além das operações de micro e macrodrenagem." /><!-- Colocar frase sobre o conteúdo do site -->\r\n    \r\n\t<meta name="DC.description" lang="pt" content="O Semae é responsável pela gestão dos serviços de captação, adução, produção, tratamento e distribuição de água potável, bem como a coleta, afastamento, tratamento e disposição final dos esgotos, além das operações de micro e macrodrenagem." /><!-- Colocar descrição do conteúdo do site em aproximadamente 20 palavras -->\r\n    \r\n\t<meta name="Abstract" content="O Semae é responsável pela gestão dos serviços de captação, adução, produção, tratamento e distribuição de água potável, bem como a coleta, afastamento, tratamento e disposição final dos esgotos, além das operações de micro e macrodrenagem." /><!-- Colocar frase sobre o conteúdo do site -->\r\n    \r\n\t<meta name="rating" content="general" />\r\n\t<meta name="robots" content="all" /><!-- Robots pegam todas as páginas -->\r\n    \r\n    <!-- Favicon --> \r\n\t<link rel="shortcut icon" href="http://www.semae.rs.gov.br/images/favicon.ico">\r\n        <link rel="stylesheet" href="http://www.semae.rs.gov.br/css/layout.css"  type="text/css" media="all"/>\r\n        <link rel="stylesheet" href="http://www.semae.rs.gov.br/css/styles.css" type="text/css" media="all" />\r\n        <link href="http://www.semae.rs.gov.br/css/skitter.styles.css" rel="stylesheet" type="text/css" />\r\n        <script type="text/javascript" language="javascript" src="http://www.semae.rs.gov.br/js/jquery-1.6.3.min.js"></script>        \r\n    \r\n    <script type="text/javascript">\r\n  // barsVisualization must be global in our script tag to be able\r\n  // to get and set selection.\r\n  var barsVisualization;\r\n\r\n  function drawMouseoverVisualization() {\r\n    var data = new google.visualization.DataTable();\r\n    data.addColumn(\'string\', \'Year\');\r\n    data.addColumn(\'number\', \'Score\');\r\n    data.addRows([\r\n      [\'2005\',3.6],\r\n      [\'2006\',4.1],\r\n      [\'2007\',3.8],\r\n      [\'2008\',3.9],\r\n      [\'2009\',4.6],\r\n    ]);\r\n\r\n    barsVisualization = new google.visualization.ColumnChart(document.getElementById(\'mouseoverdiv\'));\r\n    barsVisualization.draw(data, null);\r\n\r\n    // Add our over/out handlers.\r\n    google.visualization.events.addListener(barsVisualization, \'onmouseover\', barMouseOver);\r\n    google.visualization.events.addListener(barsVisualization, \'onmouseout\', barMouseOut);\r\n  }\r\n\r\n  function barMouseOver(e) {\r\n    barsVisualization.setSelection([e]);\r\n  }\r\n\r\n  function barMouseOut(e) {\r\n    barsVisualization.setSelection([{\'row\': null, \'column\': null}]);\r\n  }\r\n\r\n</script>\r\n\r\n <script type="text/javascript" src="https://www.google.com/jsapi"></script>\r\n    <script type="text/javascript">\r\n      google.load("visualization", "1", {packages:["corechart"]});\r\n      google.setOnLoadCallback(drawChart);\r\n      function drawChart() {\r\n        var data = google.visualization.arrayToDataTable([\r\n          [\'Data\', \'Nível\'],[\'29/02\',1.7],[\'28/02\',2],[\'27/02\',1.9],[\'26/02\',1.7],[\'25/02\',1.4]        ]);\r\n\r\n        var options = {\r\n          title: \'\',\r\n\t\r\n         \r\n        };\r\n\r\n        var chart = new google.visualization.ColumnChart(document.getElementById(\'chart_div\'));\r\n        chart.draw(data, options);\r\n      }\r\n\t  \r\n\t  function MM_jumpMenu(targ,selObj,restore){ //v3.0\r\n  eval(targ+".location=\'"+selObj.options[selObj.selectedIndex].value+"\'");\r\n  if (restore) selObj.selectedIndex=0;\r\n}\r\n\r\n    </script>\r\n    <link rel="stylesheet" href="http://www.semae.rs.gov.br/css/fancybox/jquery.fancybox-buttons.css">\r\n    <link rel="stylesheet" href="http://www.semae.rs.gov.br/css/fancybox/jquery.fancybox-thumbs.css">\r\n    <link rel="stylesheet" href="http://www.semae.rs.gov.br/css/fancybox/jquery.fancybox.css">\r\n    \r\n\t</head>\r\n\r\n<body>\r\n   \t<div class="topo" >\r\n    \t   \r\n    \t\r\n    </div>\r\n\t\r\n    <div class="cabecalho">\r\n    \r\n    \t<div class="logo">\r\n        \t<h1><a href="http://www.semae.rs.gov.br/index.php" title="SEMAE Serviço Municipal de Água e Esgotos de São Leopoldo - RS" alt="SEMAE Serviço Municipa de Água e Esgotos de São Leopoldo - RS">SEMAE Serviço Municipa de Água e Esgotos de São Leopoldo - RS</a></h1>\r\n        </div> \r\n        \t\t\r\n\t        \r\n        <div id="pesquisa">\r\n        \t <form method="post" action="http://www.semae.rs.gov.br/resultado_busca_semae.php" enctype="multipart/form-data">\r\n             \t<input  type="search" id="txtBusca" placeholder="Pesquisar..." required maxlength="50" name="busca_semae"/>\r\n        \t \t<button id="btnBusca">Buscar</button>\r\n             </form>\r\n\r\n        </div>\r\n        \r\n    </div>\r\n    \r\n\t<div class="conteudo">\r\n    \t<div id=\'cssmenu\'>\r\n           <ul>\r\n   <li><a href=\'http://www.semae.rs.gov.br/index.php\' alt="Home" title="Home"><span>HOME</span></a></li>\r\n   <li class=\'has-sub\' style="width:125px"><a href=\'#\' title="Institucional"><span>INSTITUCIONAL</span></a>\r\n      <ul>\r\n        <li><a href="http://www.semae.rs.gov.br/PortalSemae/perfil/31" title="Perfil"><span>Perfil</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/histrico/2" title="Histórico"><span>Histórico</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/misso_viso_e_valores/30" title="Missão, Visão e Valores"><span>Missão, Visão e Valores</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/visite_o_semae/3" title="Visite o Semae"><span>Visite o Semae</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/programa_de_estgio/41" title="Programa de estágio"><span>Programa de estágio</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/modelo_tarifrio_de_gua_e_esgoto/42" title="Modelo tarifário de água e esgoto"><span>Modelo tarifário de água e esgoto</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/concurso_pblico/43" title="Concurso público"><span>Concurso público</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/estrutura_administrativa/51" title="Estrutura Administrativa"><span>Estrutura Administrativa</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/leilo_n_012019/52" title="LEILÃO Nº 01/2019"><span>LEILÃO Nº 01/2019</span></a></li>\t\t\t\t\t\r\n      </ul>\r\n   </li>\r\n   \r\n    <li class=\'has-sub\'><a href=\'#\' title="Água"><span>ÁGUA</span></a>\r\n      <ul>\r\n         <li><a href="http://www.semae.rs.gov.br/PortalSemae/estrutura_do_tratamento/47" title="Estrutura do tratamento"><span>Estrutura do tratamento</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/sistema_de_abastecimento/4" title="Sistema de abastecimento"><span>Sistema de abastecimento</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/estaes_de_tratamento_de_gua/48" title="Estações de Tratamento de Água"><span>Estações de Tratamento de Água</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/ciclo_da_gua/10" title="Ciclo da água"><span>Ciclo da água</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/qualidade_da_gua/12" title="Qualidade da Água"><span>Qualidade da Água</span></a></li><li><a href="http://www.semae.rs.gov.br/entenda_sua_conta_semae.php"target=\'_parent\' title="Entenda sua conta"><span>Entenda sua conta</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/uso_consciente_da_gua/33" title="Uso consciente da água"><span>Uso consciente da água</span></a></li>\t\r\n      </ul>\r\n   </li>\r\n   \r\n    <li class=\'has-sub\'><a href=\'#\' title="Esgoto"><span>ESGOTO</span></a>\r\n      <ul>\r\n         <li><a href="http://www.semae.rs.gov.br/PortalSemae/sistema_de_tratamento_de_esgoto/49" title="Sistema de tratamento de esgoto"><span>Sistema de tratamento de esgoto</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/estaes_de_tratamento_de_esgoto/50" title="Estações de Tratamento de Esgoto"><span>Estações de Tratamento de Esgoto</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/ligao_interna_de_esgoto/14" title="Ligação Interna de Esgoto"><span>Ligação Interna de Esgoto</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/tratamento_de_esgoto_sade/15" title="Tratamento de Esgoto é Saúde"><span>Tratamento de Esgoto é Saúde</span></a></li>\t\r\n      </ul>\r\n   </li>\r\n   \r\n   <li class=\'has-sub\' style="width:140px"><a href=\'#\' title="Meio Ambiente"><span>MEIO AMBIENTE</span></a>\r\n      <ul>\r\n         <li><a href="http://www.semae.rs.gov.br/PortalSemae/projetos_ambientais/16" title="Projetos Ambientais"><span>Projetos Ambientais</span></a></li><li><a href="http://www.semae.rs.gov.br/PortalSemae/direitos_da_gua/11" title="Direitos da Água"><span>Direitos da Água</span></a></li>\t\r\n      </ul>\r\n   </li>\r\n   \r\n    <li class=\'has-sub\'><a href=\'#\' title="Serviços"><span>SERVIÇOS</span></a>\r\n      <ul>\r\n         <li><a href="http://www.semae.rs.gov.br/entenda_sua_conta_semae.php"target=\'_parent\' title="Entenda sua conta"><span>Entenda sua conta</span></a></li><li><a href="http://www.semae.rs.gov.br/http://agenciaweb.semae.rs.gov.br:2020/Fatura/SegundaViaPublica"target=\'_blank\' title="Segunda via da conta"><span>Segunda via da conta</span></a></li><li><a href="http://www.semae.rs.gov.br/certidoes_semae.php"target=\'_parent\' title="Emissão de Certidão"><span>Emissão de Certidão</span></a></li><li><a href="http://www.semae.rs.gov.br/pagamento_online_semae.php"target=\'_parent\' title="Pagamento online"><span>Pagamento online</span></a></li><li><a href="http://www.semae.rs.gov.br/debito_automatico_semae.php"target=\'_parent\' title="Débito Automático"><span>Débito Automático</span></a></li><li><a href="http://www.semae.rs.gov.br/ligacao_nova_semae.php"target=\'_parent\' title="Ligação nova de água e/ou esgoto"><span>Ligação nova de água e/ou esgoto</span></a></li><li><a href="http://www.semae.rs.gov.br/consulta_protocolo_semae.php"target=\'_parent\' title="Consulta Protocolo"><span>Consulta Protocolo</span></a></li>\t\r\n      </ul>\r\n   </li>\r\n   \r\n    <li class=\'has-sub\'><a href=\'#\' title="Links"><span>LINKS</span></a>\r\n      <ul>\r\n          <li><a href="http://portaldoservidor.semae.rs.gov.br"target=\'_blank\' title="Portal do Servidor"><span>Portal do Servidor</span></a></li><li><a href="http://www.saoleopoldo.rs.gov.br"target=\'_blank\' title="Prefeitura Municipal de São Leopoldo"><span>Prefeitura Municipal de São Leopoldo</span></a></li><li><a href=" http://www.consorcioprosinos.com.br/"target=\'_blank\' title="Pró-Sinos "><span>Pró-Sinos </span></a></li><li><a href="http://www.comitesinos.com.br/"target=\'_blank\' title="Comitesinos"><span>Comitesinos</span></a></li><li><a href=" http://www.martimpescador.org.br/"target=\'_blank\' title="Instituto Martim Pescador "><span>Instituto Martim Pescador </span></a></li><li><a href="http://www.assemae.org.br"target=\'_blank\' title="Assemae"><span>Assemae</span></a></li><li><a href="http://www.abes-dn.org.br/"target=\'_blank\' title="ABES"><span>ABES</span></a></li><li><a href=" http://www2.ana.gov.br/Paginas/default.aspx"target=\'_blank\' title="Agência Nacional de Água "><span>Agência Nacional de Água </span></a></li><li><a href="http://www.snis.gov.br/"target=\'_blank\' title="SNIS"><span>SNIS</span></a></li>\t\t  <li class=\'last\'><a href="http://www.saoleopoldo.rs.gov.br/?titulo=Portal%20Transpar%EAncia&template=hotSite&categoria=391&codigoCategoria=391&tipoConteudo=INCLUDE_MOSTRA_CONTEUDO&idConteudo=" target="_blank"><b>Portal da Transparência</b></a></li>\r\n      </ul>\r\n   </li>\r\n   \r\n    <li class=\'has-sub\' style="width:124px"><a href=\'#\' title="Fale Conosco"><span>FALE CONOSCO</span></a>\r\n      <ul>\r\n         <li><a href=\'http://www.semae.rs.gov.br/falecom_semae.php\' title="Contato"><span>Contato</span></a></li>\r\n         <li><a href=\'http://www.semae.rs.gov.br/conteudo_semae.php?menuv=18\' title="Ouvidoria"><span>Ouvidoria</span></a></li>\r\n         <li class=\'last\'><a href=\'http://www.semae.rs.gov.br/postos_atendimento_semae.php\' title="Postos de Atendimento"><span>Postos de Atendimento</span></a></li>\r\n      </ul>\r\n   </li>\r\n               \r\n</ul>        </div>\r\n                \r\n        \r\n      <div id="limpa"></div>\r\n        \r\n        <div class="conteudo_paginas">\r\n        \r\n           <div style="width:100%¨; height:22px; background:#999999; padding:5px 0px 0px 10px; font-size:10px; color:#FFFFFF; margin-bottom:10px; font-family:Arial, Helvetica, sans-serif">\r\n            \t<h3>Links / Banco de Notícias </h3>\r\n        </div>\r\n        \r\n        \r\n        \t<div class="tipo_texto" ><p class="data_noticia">21/02/2020 - 15h34<p><h1 title="Moradores do Santa Teresa participam da prestação da contas do Semae">Moradores do Santa Teresa participam da prestação da contas do Semae</h1><div class="imagens"> <a href="http://www.semae.rs.gov.br/img/grandes/21022020_152556.jpg" class="fancybox" rel="group" title=""> <img src="http://www.semae.rs.gov.br/img/pequenas/21022020_152556.jpg" alt="" title="" /></a>\r\n\t\t\t\t\t<p></p></div><p><p>Na noite de quinta-feira, 20 de fevereiro, aconteceu a 4&ordf; Rodada de Presta&ccedil;&atilde;o de Contas do Semae, desta vez na Associa&ccedil;&atilde;o de Moradores da Vila Justo, na Rua Viam&atilde;o, no bairro de Santa Teresa,&nbsp; Zona Sul de S&atilde;o Leopoldo. O evento, que vai percorrer todas as regi&otilde;es do munic&iacute;pio at&eacute; abril, tem como objetivos apresentar as realiza&ccedil;&otilde;es da autarquia no per&iacute;odo de 2017-2020 e ouvir sugest&otilde;es e demandas da comunidade para melhorar os servi&ccedil;os.&nbsp;</p>\r\n\r\n<p>O in&iacute;cio da atividade se deu com a apresenta&ccedil;&atilde;o de rap de tr&ecirc;s adolescentes que s&atilde;o alunos da Oficina de Comunica&ccedil;&atilde;o Comunit&aacute;ria, do projeto Guardi&otilde;es da &Aacute;gua, na Ocupa&ccedil;&atilde;o da Justo. Eles t&ecirc;m aulas com o oficineiro Mano Vini. Os jovens Nego Vini, Paj&eacute; e Naruto, al&eacute;m de fazerem a apresenta&ccedil;&atilde;o art&iacute;stica inicial e final do evento, tamb&eacute;m deram depoimentos sobre a import&acirc;ncia do projeto Guardi&otilde;es da &Aacute;gua para a comunidade e para as suas vidas pessoais.&nbsp;</p>\r\n\r\n<p>O evento iniciou com a apresenta&ccedil;&atilde;o de um v&iacute;deo institucional que mostra as principais conquistas do Semae nos &uacute;ltimos anos, detalha alguns dos investimentos e explica porque S&atilde;o Leopoldo, apesar da seca, est&aacute; num patamar de pleno abastecimento de &aacute;gua, sem risco eminente de racionamento.</p>\r\n\r\n<p>Em sua sauda&ccedil;&atilde;o inicial, o diretor-geral do Semae, Nestor Schwertner, lembrou que Santa Tereza, por ser uma das regi&otilde;es topograficamente mais altas da cidade, como a Vila Nova, sempre sofreu com falta d&rsquo;&aacute;gua. &ldquo;N&oacute;s, desde 2017, trabalhamos muito para resolver esse problema. Antes, quando o Rio dos Sinos chegava ao n&iacute;vel de 1 metro e 10 cent&iacute;metros, j&aacute; ficava dif&iacute;cil bombear &aacute;gua para as regi&otilde;es mais altas. Hoje, com a nossa nova capta&ccedil;&atilde;o, na nova EAB, temos uma tecnologia mais eficiente que d&aacute; seguran&ccedil;a mesmo que tenhamos n&iacute;veis muito baixos no rio. Podemos afirmar que s&oacute; falta &aacute;gua na cidade se o Rio dos Sinos secar completamente. A falta de &aacute;gua hoje s&oacute; se d&aacute; por eventuais problemas de falta de energia el&eacute;trica ou rompimentos de tubula&ccedil;&atilde;o&rdquo;, garantiu Nestor.</p>\r\n\r\n<p>O assessor de Gest&atilde;o Organizacional do Semae, Anderson Etter, apresentou dados e imagens das a&ccedil;&otilde;es da autarquia na Regi&atilde;o Sul de S&atilde;o Leopoldo. &ldquo;Nada &eacute; mais correto do que o Semae estar nas associa&ccedil;&otilde;es de moradores, nas igrejas, juntos das comunidades, apresentar o seu trabalho e, principalmente, ouvir as demandas da popula&ccedil;&atilde;o. Estamos prestando contas dos investimentos e melhorias realizados e como estamos revertendo os recursos financeiros oriundos dos pagamentos das tarifas de &aacute;gua de cada resid&ecirc;ncia. &Eacute; importante que o Semae, como empresa p&uacute;blica, fa&ccedil;a isso &ndash; queremos mostrar que a empresa p&uacute;blica funciona, &eacute; um patrim&ocirc;nio do povo de S&atilde;o Leopoldo e d&aacute; resultados&rdquo;, disse.&nbsp;</p>\r\n\r\n<p>Em 31 de dezembro de 2016, no &uacute;ltimo dia da gest&atilde;o passada, o Semae foi deixado com uma d&iacute;vida de mais de R$ 37 milh&otilde;es. Desde montante, R$ 10 milh&otilde;es eram de d&iacute;vidas com a companhia de energia el&eacute;trica. O saldo em caixa do Semae, no fim de 2016 era de apenas R$ 85 mil. Hoje, o saldo em caixa da autarquia &eacute; de R$ 7 milh&otilde;es, sendo que neste per&iacute;odo j&aacute; foram pagos mais de R$ 18 milh&otilde;es da d&iacute;vida anterior. Tudo isso sem abdicar de investimentos. &ldquo;Na Regi&atilde;o Sul h&aacute; 8.921 economias (resid&ecirc;ncias com medi&ccedil;&atilde;o de consumo de &aacute;gua) e 395 fam&iacute;lias s&atilde;o beneficiadas, desde 2017, com a Tarifa Social que possibilita que paguem um pre&ccedil;o mais justo pela &aacute;gua de acordo com sua renda&rdquo;, detalhou Anderson.&nbsp;</p>\r\n\r\n<p>A l&iacute;der comunit&aacute;ria e servidora p&uacute;blica T&acirc;nia Corr&ecirc;a, que &eacute; moradora h&aacute; 50 anos do bairro Santa Teresa, lembrou dos problemas hist&oacute;ricos de falta d&rsquo;&aacute;gua na regi&atilde;o &ndash; que est&atilde;o resolvidos. &ldquo;Nos &uacute;ltimos anos, nunca mais faltou &aacute;gua. Por isso, est&atilde;o de parab&eacute;ns&rdquo;, disse T&acirc;nia. O aposentado Almeri Garcia, morador do local h&aacute; 46 anos, tamb&eacute;m lembrou que o problema era cr&ocirc;nico: &ldquo;Eu acho que o trabalho est&aacute; excelente, n&atilde;o temos do que nos queixar&rdquo;. O servidor do Hospital Centen&aacute;rio Jorge Ortiz, que mora no bairro h&aacute; 3 anos, ressaltou que neste per&iacute;odo n&atilde;o teve problema com abastecimento de &aacute;gua.&nbsp;</p>\r\n\r\n<p>Em seguida, se sucederam no microfone os oficineiros do projeto Guardi&otilde;es da &Aacute;gua Wagner Coriolano e Andr&eacute; de Jesus que ressaltaram a import&acirc;ncia de uma autarquia de &aacute;gua e esgoto, como o Semae, investir tamb&eacute;m em educa&ccedil;&atilde;o ambiental atrav&eacute;s de projetos de arte e cultura.&nbsp;</p>\r\n\r\n<p>Em sua fala final, o diretor-geral do Semae Nestor Schwertner pontuou alguns aspectos da atual gest&atilde;o como o investimento em efici&ecirc;ncia hidroenerg&eacute;tica &ndash; que economiza energia el&eacute;trica e reduz o desperd&iacute;cio de &aacute;gua tratada perdida em vazamentos. &ldquo;Estamos certos de que fazendo a substitui&ccedil;&atilde;o das redes mais antigas de &aacute;gua, economizamos mais de 20%, 25% da &aacute;gua. Perdendo menos &aacute;gua, podemos captar menos e, assim, economizar tamb&eacute;m produtos qu&iacute;micos no tratamento da &aacute;gua para o consumo&rdquo;, explicou Nestor. &ldquo;A &aacute;gua &eacute; um bem p&uacute;blico universal e pertence, portanto, a todas as pessoas. Por isso &eacute; importante mantermos o Semae uma empresa p&uacute;blica, com bons servi&ccedil;os, para atender ao povo de S&atilde;o Leopoldo&rdquo;, concluiu.&nbsp;</p>\r\n\r\n<p>Depois de uma breve pausa na semana do Carnaval, as Rodadas de Presta&ccedil;&atilde;o de Contas do Semae voltar&atilde;o a acontecer na primeira semana de mar&ccedil;o, na Zona Norte de S&atilde;o Leopoldo.</p>\r\n</p><div id="limpa"></div><h1 style="margin-top:30px">Últimas Noticías</h1><p class="data_noticia">29/02/2020&nbsp;&nbsp;&nbsp;<a href="http://www.semae.rs.gov.br/noticias_detalhes_semae.php?idnoticia=805" class="link_noticias" title="Semae realiza atividade para apresentar os benefícios do Programa de Substituição de Redes">Semae realiza atividade para apresentar os benefícios do Programa de Substituição de Redes</a></p><p class="data_noticia">28/02/2020&nbsp;&nbsp;&nbsp;<a href="http://www.semae.rs.gov.br/noticias_detalhes_semae.php?idnoticia=804" class="link_noticias" title="Investimentos garantem abastecimento apesar da estiagem">Investimentos garantem abastecimento apesar da estiagem</a></p><p class="data_noticia">19/02/2020&nbsp;&nbsp;&nbsp;<a href="http://www.semae.rs.gov.br/noticias_detalhes_semae.php?idnoticia=802" class="link_noticias" title="Vila Nova teve encontro de prestação de contas do Semae">Vila Nova teve encontro de prestação de contas do Semae</a></p><p class="data_noticia">14/02/2020&nbsp;&nbsp;&nbsp;<a href="http://www.semae.rs.gov.br/noticias_detalhes_semae.php?idnoticia=801" class="link_noticias" title="Escola Olímpio Albrecht, da Feitoria, recebeu segunda rodada de prestação de contas">Escola Olímpio Albrecht, da Feitoria, recebeu segunda rodada de prestação de contas</a></p><p class="data_noticia">12/02/2020&nbsp;&nbsp;&nbsp;<a href="http://www.semae.rs.gov.br/noticias_detalhes_semae.php?idnoticia=800" class="link_noticias" title="Começa a rodada de prestação de contas">Começa a rodada de prestação de contas</a></p></div>\t\r\n            \r\n             <h1 style="margin-top:20px;" title="Fale com o Semae">Notícias SEMAE</h1>\r\n            <a href="http://www.semae.rs.gov.br/noticias_semae.php" class="link_noticias">Utilize esta página para pesquisar nosso banco de dados de notícias</a>\r\n    </div>    \r\n    \r\n    <div class="coluna_direita">\r\n   \t\t<div class="servicos_online">\r\n     <h1 title="SERVIÇOS ON-LINE">SERVIÇOS ON-LINE</h1> \r\n     <p style="margin-bottom:5px;">Solicite serviços sem sair de casa.</p>\r\n     <div class="formulario1">\r\n     \t<ul>\r\n            <li><a href="http://www.semae.rs.gov.br/entenda_sua_conta_semae.php" title="Entenda sua conta">Entenda sua conta</a></li>\r\n            <!--<li><a href="http://www.semae.rs.gov.br/segunda_via_conta_semae.php" title="Segunda via da conta">Segunda via da conta</a></li>-->\r\n\t\t\t<li><a href="http://agenciaweb.semae.rs.gov.br:2020/Fatura/LoginSegundaViaPublica" target="_blank" class="link_noticias">Segunda via da conta</a></li>\r\n            <li><a href="http://www.semae.rs.gov.br/certidoes_semae.php" title="Emissão de Certidões">Emissão de Certidões</a></li>\r\n\t\t\t<li><a href="http://www.semae.rs.gov.br/pagamento_online_semae.php" title="Pagamento online">Pagamento online</a></li>\r\n            <li><a href="http://www.semae.rs.gov.br/debito_automatico_semae.php" title="Débito Automático">Débito Automático</a></li>\r\n            <li><a href="http://www.semae.rs.gov.br/ligacao_nova_semae.php" title="Ligação nova de água e/ou esgoto">Ligação nova de água e/ou esgoto</a></li>\r\n            <!--<li><a href="http://www.semae.rs.gov.br/consulta_debitos_semae.php" title="Consulte seus débitos">Consulte seus débitos</a></li>\r\n            <li><a href="historico_consumo_semae.php" title="Histórico de consumo">Histórico de consumo</a></li>\r\n            <li><a href="certidao_negativa_semae.php" title="Certidão negativa">Certidão negativa</a></li> -->\r\n         </ul>\r\n     </div>\r\n </div>\r\n \r\n <div id="limpa"></div>\r\n \r\n  <div class="nivel_rio1">\r\n    <h1 title="Nível do  Rio dos Sinos">Nível do  Rio dos Sinos</h1>\r\n    <div id="chart_div" style="width: 200px; height: 130px;"></div>\r\n    <p>* Medição realizada às 7 horas no ponto de captação do Semae.</p>\r\n</div>\r\n\r\n<div style="float:right; height:300px">\r\n    <div class="destaques_0800">\r\n    \t<img src="http://www.semae.rs.gov.br/img/semae_0800.jpg" alt="Ligação Gratuita 0800 510 2910" title="Ligação Gratuita 0800 510 2910" />\r\n        <!-- <h1 title="Siga-nos">Siga-nos</h1>       \r\n        <img src="http://semae.web811.uni5.net/img/facebook_semae.png" alt="Facebook Semae" title="Facebook Semae" />\r\n        <img src="http://semae.web811.uni5.net/img/youtube_semae.png" alt="Canal Youtube Semae" title="Canal Youtube Semae" />\r\n        <img src="http://semae.web811.uni5.net/img/twitter_semae.png" alt="Twitter Semae" title="Twitter Semae" /> -->\r\n    </div>\r\n   \r\n</div>    \r\n    </div>\r\n    \r\n    <div id="limpa"></div>\r\n         \r\n</div>\r\n            \r\n   \t<div class="rodape">\r\n    \t<div class="rodape_box">\r\n        <div class="rodape_coluna2">\r\n            <h2 title="Unidades de Atendimento">Unidade de Atendimento</h2>\r\n            \r\n            <ul>\r\n            \r\n             <li><h3 title="SEMAE - Centro">SEMAE - Centro</h3><p>Rua João Neves da Fontoura, 811 - Centro</p></li>               \r\n            </ul>\r\n        </div>\r\n    \r\n        <div class="rodape_coluna3">  \r\n            <div class="destaques_semae">\r\n                <img src="http://www.semae.rs.gov.br/img/logo_semae_rodape.png" alt="SEMAE Serviço Municipal de Água e Esgotos de São Leopoldo - RS" title="SEMAE Serviço Municipal de Água e Esgotos de São Leopoldo - RS" />                \r\n            </div>  \r\n                                          \r\n            <div class="destaques_pmsl">\r\n                <a href="https://www.saoleopoldo.rs.gov.br/" target="_blank">\r\n                    <img src="http://www.semae.rs.gov.br/img/pmsl_logo.png" alt="Prefeitura Municipal de São Leopoldo-RS" title="Prefeitura Municipal de São Leopoldo-RS" />                </a>\r\n            </div>\r\n            \r\n      </div>\r\n</div>\t</div>\r\n\r\n       <!-- FancyBox -->\r\n\t\t<script src="http://www.semae.rs.gov.br/js/fancybox/jquery.fancybox.js"></script>\r\n\t\t<script src="http://www.semae.rs.gov.br/js/fancybox/jquery.fancybox-buttons.js"></script>\r\n\t\t<script src="http://www.semae.rs.gov.br/js/fancybox/jquery.fancybox-thumbs.js"></script>\r\n        <script src="http://www.semae.rs.gov.br/js/fancybox/jquery.easing-1.3.pack.js"></script>\r\n\t\t<script src="http://www.semae.rs.gov.br/js/fancybox/jquery.mousewheel-3.0.6.pack.js"></script>\r\n        \r\n        <script type="text/javascript">\r\n\t\t\t$(document).ready(function() {\r\n\t\t\t$(".fancybox").fancybox();\r\n\t\t\t});\r\n\t\t</script>       \r\n    \r\n</body>\r\n</html>\r\n'''

        semae = SEMAE()
        self.assertEqual(semae.getPageHtml(803), html)

if __name__ == '__main__':
    unittest.main()