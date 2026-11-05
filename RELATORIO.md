# Interface Genesis no Poupa Grana

Aplicada à pasta indicada: C:/Users/GEOVANE PAIXÃO/Downloads/poupa-grana.

Alterados: templates base, login e painel; paleta do gráfico. Adicionados genesis.css e globe.js. Visual preto e verde, painéis translúcidos, botões luminosos e globo em canvas local. Identidade Poupa Grana preservada. Nenhum endpoint, modelo, cálculo financeiro, configuração, autenticação ou permissão alterado.

Validação: 75 testes passaram em PostgreSQL temporário isolado, Ruff aprovado, JavaScript com sintaxe válida. Uma advertência do pytest sobre escrita de cache não afetou os testes. A primeira tentativa de testes falhou por configuração/acesso ao banco local; a suíte foi então executada com sucesso em cluster descartável próprio, encerrado ao final. Preview renderizado com os templates Django e dados fictícios zerados, sem login em dados reais. Desktop e celular (390 px) conferidos, sem overflow horizontal global ou erros de JavaScript; contraste do título do login corrigido durante a conferência.

Backup dos quatro arquivos existentes: ../poupa-grana-interface-anterior.zip. Os dois novos arquivos são genesis.css e globe.js. Os seis arquivos aplicados em Downloads foram comparados por SHA-256 com a versão validada.

A pasta em Downloads não contém repositório Git próprio; não foi alterado o Git pai, nem criado commit, PR, CI remoto ou deploy. A cópia de trabalho está em ../poupa-grana-genesis. Os arquivos .env, bancos e credenciais não estão no pacote de entrega.

Reprodução: usar o ambiente Python e PostgreSQL do projeto; executar iniciar.cmd. Se o navegador mantiver o tema anterior em cache, usar Ctrl+F5. Para os testes, definir TEST_DATABASE_URL com um PostgreSQL descartável e executar python -m pytest -q; python -m ruff check .

Limite: as conferências visuais usaram dados fictícios e não incluíram submissão de formulários com dados reais. A mudança é visual, sem reconstrução de backend.

Aguardo sua conferência antes do merge.
