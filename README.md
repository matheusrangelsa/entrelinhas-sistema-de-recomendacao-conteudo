# Projeto Entrelinhas | Sistema de Recomendação de Conteúdos de Streaming
Projeto desenvolvido para implementar as **funcionalidades básicas** do sistema de recomendação de um streaming de vídeos, baseado na **filtragem por conteúdo** usando **python**.

O código está sendo melhorado ainda, mas por enquanto se seguir as instruções corretamente, conseguirá receber filmes recomendados ao executar o código.




### **Etapas do algoritmo:**
---
   1.  Ler um arquivo CSV com informações sobre filmes;
   2.  Solicitar ao usuário o tempo disponível para assistir filmes;
   3.  Perguntar ao usuário qual dos gêneros de filmes disponíveis é o seu favorito;
   4.  Aplicar o primeiro filtro e gera uma pré-lista com os filmes que atendam às condições escolhidas de tempo x gêneros (incluída a a função "random.shuffle" do módulo "random" para embaralhar a ordem da lista antes de retorná-la);
   5.  Aplicar o segundo filtro que seleciona os filmes cuja soma das durações é menor ou igual ao tempo disponível informado pelo usuário;
   6.  Formatar a saída da lista de recomendações de filmes, exibindo o resultado das recomendações.
<br><br>
> **CUIDADO:** sempre busque atualizar o caminho do arquivo CSV (*filmes_projeto.csv*), pois dependendo do local que seja utilizado para rodar o código pode dar erro pois o arquivo não será encontrado se o ajuste de 'caminho' do CSV não for feito nos trechos de código das variáveis **datatset* e *data_set* dentro da seção "Executando o algoritmo de recomendação".

<br><br>
*Recomendo alterar para o tema dark ao visualizar o código no Google Colab :)*
