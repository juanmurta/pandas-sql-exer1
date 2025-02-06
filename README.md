# Análise de Salários com SQLite e Pandas  

## Descrição  
Este script conecta-se a um banco de dados SQLite contendo informações salariais, extrai os dados da tabela `Salaries` e realiza análises, como:  
- Filtragem de registros para a agência "San Francisco".  
- Cálculo da média salarial por ano.  
- Contagem do número de registros por ano.  
- Cálculo do total pago em salários e benefícios por ano.  

## Como Usar  

1. **Pré-requisitos**  
   - Ter o SQLite instalado e um banco de dados chamado `salarios.sqlite`.  
   - Instalar as bibliotecas necessárias executando:  

     ```bash
     pip install pandas pyodbc
     ```  

2. **Estrutura do Banco de Dados**  
   O script espera uma tabela chamada `Salaries` no banco de dados SQLite com pelo menos as seguintes colunas:  

   - **Id**: Identificador único do funcionário.  
   - **Agency**: Nome da agência.  
   - **Year**: Ano do pagamento.  
   - **TotalPay**: Salário base total.  
   - **TotalPayBenefits**: Salário total incluindo benefícios.  

3. **Execução do Script**  
   - Certifique-se de que o banco de dados `salarios.sqlite` está localizado no diretório correto.  
   - Execute o script no terminal ou em um ambiente Python:  

     ```bash
     python nome_do_arquivo.py
     ```  

## Contribuindo para o projeto  
1. Para contribuir com este projeto, siga estas etapas:  
2. Bifurque este repositório.  
3. Crie um branch: `git checkout -b <nome_branch>`.  
4. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`.  
5. Envie para o branch original: `git push origin <nome_do_projeto>/<local>`.  
6. Crie a solicitação de pull.  

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).  
