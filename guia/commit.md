## Commits

:information_source:  Commits são salvamentos de versões do código em um projeto, permitindo reverter mudanças específicas ou entender o que foi feito em cada versão.

##### Como efetuar um commit

Para efetuar um commit, você precisará adicionar as alterações que deseja incluir no commit à área de stage do Git:

```
git add arquivo_alterado
```

Em seguida, execute o comando git commit, escrevendo uma mensagem que descreva as alterações realizadas no arquivo:

```
git commit -m ":books: docs: Editar nome do arquivo"
```

Por fim, envie o commit para o repositório:

```
git push
```
<hr>

## Commits Semânticos

Commits Semânticos são uma convenção para padronizar mensagens de commit e tornar o histórico de commits mais explícito, facilitando a criação de ferramentas automatizadas. Eles ajudam a entender facilmente as alterações realizadas em um trecho de código.

O commit semântico possui os elementos estruturais abaixo (tipos), que informam a intenção do seu commit ao utilizador(a) de seu código.

  
- `feat`- Commits do tipo feat indicam que seu trecho de código está incluindo um **novo recurso** (se relaciona com o MINOR do versionamento semântico).

- `fix` - Commits do tipo fix indicam que seu trecho de código commitado está **solucionando um problema** (bug fix), (se relaciona com o PATCH do versionamento semântico).

- `docs` - Commits do tipo docs indicam que houveram **mudanças na documentação**, como por exemplo no Readme do seu repositório. (Não inclui alterações em código).

- `test` - Commits do tipo test são utilizados quando são realizadas **alterações em testes**, seja criando, alterando ou excluindo testes unitários. (Não inclui alterações em código)

- `build` - Commits do tipo build são utilizados quando são realizadas modificações em **arquivos de build e dependências**.

- `perf` - Commits do tipo perf servem para identificar quaisquer alterações de código que estejam relacionadas a **performance**.

- `style` - Commits do tipo style indicam que houveram alterações referentes a **formatações de código**, semicolons, trailing spaces, lint... (Não inclui alterações em código).

- `refactor` - Commits do tipo refactor referem-se a mudanças devido a **refatorações que não alterem sua funcionalidade**, como por exemplo, uma alteração no formato como é processada determinada parte da tela, mas que manteve a mesma funcionalidade, ou melhorias de performance devido a um code review.

- `chore` - Commits do tipo chore indicam **atualizações de tarefas** de build, configurações de administrador, pacotes... como por exemplo adicionar um pacote no gitignore. (Não inclui alterações em código)

- `ci` - Commits do tipo ci indicam mudanças relacionadas a **integração contínua** (_continuous integration_)
 

<hr>

### :sparkles:  Boas práticas 
Para manter o histórico de commits organizado e fácil de entender, é importante seguir alguns padrões de commit. Algumas dicas são:

* :bulb: Escreva mensagens de commit claras e concisas, que expliquem o que foi feito e por quê.

* :bulb: Use o infinitivo no título da mensagem (ex: "Adicionar feature X", "Corrigir bug Y"). Uma boa forma de se entender isso, é perguntar-se o que essa alteração irá fazer. 

* :bulb: Evite usar frases como "e outras coisas" ou "e mais algumas coisas". Se houver mais de uma alteração, crie um commit separado para cada uma delas.

<hr>

## 💈 Padrões de emojis
<br>

| Tipo de commit                  	| Emojis               	| Palavra-chave 	|
|---------------------------------	|----------------------	|---------------	|
| Acessibilidade                  	| ♿ `:wheelchair:`      	|               	|
| Adicionando um teste            	| ✅ `:white_check_mark:`	| test          	|
| Adicionando uma dependência     	| ➕ `:heavy_plus_sign:` 	| build         	|
| Alterações de revisão de código 	| 👌 `:ok_hand:`         	| style         	|
| Animações e transições          	| 💫 `:dizzy:`           	|               	|
| Bugfix                          	| 🐛 `:bug:`             	| fix           	|
| Comentários                     	| 💡 `:bulb:`            	| docs          	|
| Commit inicial                  	| 🎉 `:tada:`            	| init          	|
| Configuração                    	| 🔧 `:wrench:`          	| chore         	|
| Deploy                          	| 🚀 `:rocket:`          	|               	|
| Documentação                    	| 📚 `:books:`           	| docs          	|
| Em progresso                    	| 🚧 `:construction:`    	|               	|
| Estilização de interface        	| 💄 `:lipstick:`        	| feat          	|
| Infraestrutura                  	| 🧱 `:bricks:`          	| ci            	|
| Lista de ideias (tasks)         	| 🔜  `:soon:`           	|               	|
| Mover/Renomear                  	| 🚚 `:truck:`           	| chore         	|
| Novo recurso                    	| ✨ `:sparkles:`        	| feat          	|
| Package.json em JS              	| 📦 `:package:`         	| build         	|
| Performance                     	| ⚡ `:zap:`             	| perf          	|
| Refatoração                     	| ♻️ `:recycle:`         	| refactor      	|
| Removendo um arquivo            	| 🔥 `:fire:`            	|               	|
| Removendo uma dependência       	| ➖ `:heavy_minus_sign:`	| build         	|
| Responsividade                  	| 📱 `:iphone:`          	|               	|
| Revertendo mudanças             	| 💥 `:boom:`            	| fix           	|
| Segurança                       	| 🔒️ `:lock:`            	|               	|
| SEO                             	| 🔍️ `:mag:`             	|               	|
| Tag de versão                   	| 🔖 `:bookmark:`        	|               	|
| Teste de aprovação              	| ✔️ `:heavy_check_mark:`	| test          	|
| Testes                          	| 🧪 `:test_tube:`       	| test          	|
| Texto                           	| 📝 `:pencil:`          	|               	|
| Tipagem                         	| 🏷️ `:label:`           	|               	|
| Tratamento de erros             	| 🥅 `:goal_net:`        	|               	|


<hr>

## Estrutura do commit
Com base nessas informações, utilize sempre a seguinte estrutura em seus commits:

```
:emoji: tipo: Verbo infinitivo + descrição concisa
```

## Exemplos

| Comando git                                                           	| Resultado no GitHub                              	|
|:-----------------------------------------------------------------------	|:--------------------------------------------------	|
| `git commit -m ":tada: Commit inicial"`                                	| 🎉 Commit inicial                                 	|
| `git commit -m ":books: docs: Atualizaçao do README"`                  	| 📚 docs: Atualizar README                    		|
| `git commit -m ":bug: fix: Loop infinito na linha 50"`                 	| 🐛 fix: Corrigir Loop na linha 50                 	|
| `git commit -m ":sparkles: feat: Pagina de login"`                     	| ✨ feat: Adicionar Pagina de login                  	|
| `git commit -m ":bricks: ci: Modificaçao no Dockerfile"`               	| 🧱 ci: Modificar Dockerfile                  		|
| `git commit -m ":recycle: refactor: Passando para arrow functions"`    	| ♻️ refactor: Alterar tipo de dados Model        	|
| `git commit -m ":zap: perf: Melhoria no tempo de resposta"`            	| ⚡ perf: Melhorar tempo de resposta            		|
| `git commit -m ":boom: fix: Revertendo mudanças ineficientes"`         	| 💥 fix: Reverter mudanças ineficientes          	|
| `git commit -m ":lipstick: feat: Estilizaçao CSS do formulario"`       	| 💄 feat: Estilizar CSS do formulario            	|
| `git commit -m ":test_tube: test: Criando novo teste"`                 	| 🧪 test: Criar novo teste                       	|
| `git commit -m ":bulb: docs: Comentários sobre a função LoremIpsum( )"`	| 💡 docs: Comenar função LoremIpsum( ) 			|

<hr>

Créditos: [Iuricode](https://github.com/iuricode/padroes-de-commits)
