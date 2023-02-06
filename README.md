# Projeto Entrelinhas | Sistema de Recomendação de Conteúdos de Streaming
Projeto desenvolvido para implementar as **funcionalidades básicas** do sistema de recomendação de um streaming de vídeos, baseado na **filtragem por conteúdo** usando **python**.

O código está sendo melhorado ainda, mas por enquanto se seguir as instruções corretamente, conseguirá receber filmes recomendados ao executar o código.




### **Etapas do algoritmo:**
---
   1.  Ler um arquivo CSV com informações sobre filmes;
   2.  Solicitar ao usuário o tempo disponível para assistir filmes;
   3.  Perguntar ao usuário qual dos gêneros de filmes disponíveis é o seu favorito;
   4.  Aplicar o primeiro filtro e exibir uma lista de filmes que atendam às condições escolhidas;
   5.  Converter os valores da coluna "Duração" de string para inteiro e adicionar à uma nova lista;
   6.  Aplicar o segundo filtro que seleciona os filmes cuja soma das durações é menor ou igual ao tempo disponível informado pelo
    usuário;
   7.  Otimizar o segundo filtro incluindo um loop while para buscar outras combinações viáveis (quando houver mais de uma opção);
   8.  Formatar a saída da lista de recomendações de filmes, exibindo apenas o título dos filmes;
   9.  Perguntar ao usuário se deseja atualizar a recomendação ou encerrar o sistema;
   10.  Exibir o filtro final com a última recomendação e armazenar a lista final para futuros acessos.

<br><br><br>
*Recomendo alterar para o tema dark ao visualizar o código no Google Colab :)*
