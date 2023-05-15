# api_ecommerce_python_django
<br>
API de organização REST desenvolvida em Python e Django, integrada ao banco de dados PostgreSQL. Feita com Django Rest Framework (DRF), Generic Views, validação de dados e documentação. Possui paginação em rotas de listagem, sendo algumas rotas protegidas, com permissões distintas para admin, vendedor e cliente, utilizando JSON Web Token (JWT) e o usuário padrão do Django(AbstractUser)<br><br>
MVP feito por: Gabriel Machado, Gabriela Fontoura, Guileano Gadea, Victor Guterres em cerca de 7 dias <br><br>

Banco de dados estruturado nas tabelas: users, addresses, products, cart, orders, que estabelacem relacionamentos 1:1, 1:N e N:N.<br>
Possui 19 endpoints que viabilizam rotas básicas de manipulação de dados (CRUD) <br>
<br>
Diagrama Entidades e Relacionamentos: <br>
![DER](https://github.com/gabifontoura/api_ecommerce_python_django/assets/110035918/ebd70296-6720-4904-a46d-0dba321effd6)
<br><br>
Deploy (URL base): https://ecommerce-g42.onrender.com/  <br>
Documentação: https://ecommerce-g42.onrender.com/api/docs/swagger/

# Rotas que não precisam de autenticação

<h2> Criação de usuário </h2>
 
 Nessa aplicação o usuário pode se cadastrar utilizando seu primeiro e último nome, seu nome de usuário e como padrão a role(função) dele
 vem como cliente(apenas administradores podem criar outros administradores e vendedores) .

```json
{
		"first_name": "Pedro",
		"last_name": "Castro",
		"email": "Pc@mail.com",
		"username": "PcGamerSP",
		"password": "1234"
}

```

`POST /users - FORMATO DA RESPOSTA - STATUS 201`

```json
{               
                "id":1
		"first_name": "Pedro",
		"last_name": "Castro",
		"role": "Client",
		"email": "Pc@mail.com",
		"username": "PcGamerSP"
}

```
em caso de erro:

```json
{
	"first_name": [
		"This field is required."
	],
	"last_name": [
		"This field is required."
	],
	"username": [
		"This field is required."
	],
	"email": [
		"This field is required."
	],
	"password": [
		"This field is required."
	]
}
```

<h2> Login de usuário </h2>


body:

```json
       {
	"username": "John Doe",	
	"password":1234
	}
```


`POST /users/login - FORMATO DA RESPOSTA - STATUS 201`

```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NDI0NzU4MiwiaWF0IjoxNjgzNjQyNzgyLCJqdGkiOiJhNGM0YzdhN2YxNjg0NmU4ODczNTFmYTJkOWY1NDkxMyIsInVzZXJfaWQiOjJ9.17ZJeaNgKZH5A4OclYufT_ErMIKcr_g8zjLm6Th36Jo",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNjk2NzgyLCJpYXQiOjE2ODM2NDI3ODIsImp0aSI6ImFmYzkzYWVkOGEzOTQwMDVhODM3Yzk5ZGVlOTlkMjk3IiwidXNlcl9pZCI6Mn0.xqTLZBTDdIuBcLGSBxpj4BCVFKgu-UbOxw1Nu-s24Aw"
}
```

<h2> Lista de Produtos  </h2>

Na rota /products/ qualquer usuário é capaz de ter acesso a lista de produtos 



`GET /products/ - FORMATO DA RESPOSTA - STATUS 200`

```json

{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"name": "homem-aranha",
			"category": "brinquedo",
			"value": "200.00",
			"quantity": 20,
			"is_available": true,
			"image": null,
			"seller_id": 4
		},
		{
			"id": 2,
			"name": "caminhão",
			"category": "carrinho",
			"value": "120.00",
			"quantity": 10,
			"is_available": true,
			"image": null,
			"seller_id": 4
		}
	]
}

```




# Rotas que precisam de autenticação

<h2> Lista de todos os usuários </h2>
 
 Nessa aplicação o usuário deve ser administrador para poder listar os usuários .
 
 ` GET /users/all - FORMATO DA RESPOSTA - STATUS 200`

```json
	"count": 2,
	"next": null,
	"previous": null,
	"results"[
{
		"first_name": "Pedro",
		"last_name": "Castro",
		"role": "Client",
		"email": "Pc@mail.com",
		"username": "PcGamerSP"
},
{
		"first_name": "Larissa",
		"last_name": "Torres",
		"role": "Client",
		"email": "Kenzie@mail.com",
		"username": "Random"
},
]
```
Lembrando que no cabeçalho da resposta, temos as informações sobre a paginação, e o nextUrl para acessar a próxima página.

Cabeçalho da resposta:

> count: <br/>
> page:  <br/>
> perPage: 

Em caso de erro na autorização ou caso o usuário não passe o token de autorização na requisição:

` GET /users/all - FORMATO DA RESPOSTA - STATUS 401 unauthorized`


```json

{
	"detail": "You do not have the authorization to perform this action."
}


```
<h2> Atualização e deleção de usuários </h2>

Utilizandoa a rota /users/:id é possível fazer a pesquisa do usuário, update e o delete pegando o id do usuário, somente o usuário
, com exceção do admin pode editar e deletar o próprio delete, caso o usuário tente atualizar o perfil de outro usuário .

essa requisição não precisa de um corpo

` GET /users/:id - FORMATO DA RESPOSTA - STATUS 200 `


```json

{
		
	"email": "Pc@Gmail.com"
}


```

```json
{		"id":1
		"first_name": "Pedro",
		"last_name": "Castro",
		"role": "Client",
		"email": "Pc@Gmail.com",
		"username": "PcGamerSP"
}

```
em caso de erro na autorização:



```json
{
	"detail": "You do not have the authorization to perform this action."
}
```

<h2> Criação de endereços para os usuários </h2>

Nessa rota /addresses o usuário é capaz de registrar o seu próprio endereço, 
na rota /addresses/:id editar e deletar o seu próprio endereço, caso o usuário tente editar 
o endereço de outro usuário que não seja ele mesmo e ele não seja administrador ele será barrado.


```json

{
	"street":"P.O. Box 340, 1023 Arcu. Ave",
	"number":"838",
	"city":"Colombo",
	"state":"PR"
}

```

` POST /addresses - FORMATO DA RESPOSTA - STATUS 200 `

```json
{	"id": 1,
	"street": "P.O. Box 340, 1023 Arcu. Ave",
	"number": "838",
	"city": "Colombo",
	"state": "PR",
	"user_id": 3
}

```

```json
{
	"number":"20"
}

```


`PATCH /addresses/:id - FORMA DA RESPOSTA - STATUS 200 `


```json
{
	"id": 1,
	"street": "P.O. Box 340, 1023 Arcu. Ave",
	"number": "20",
	"city": "Colombo",
	"state": "PR",
	"user_id": 3
}
```
Em caso de erro na autorização:

```json
{
	"detail": "You do not have permission to perform this action."
}
```

`DEL /addresees/:id - FORMA DA RESPOSTA - STATUS 204 NO CONTENT`


```json
{
	"detail": "You do not have permission to perform this action."
}
```

<h2> Criação de produtos </h2>

Na rota products/add/ o usuário sendo seller ou admin é capaz de criar um produto


```json
"name": "homem-aranha",
"category": "brinquedo",
"value": "200.00",
"quantity": 20,
```

`POST /products/add - FORMA DA RESPOSTA - STATUS 200 `


```json

{	

	"id": 1,
	"name": "homem-aranha",
	"category": "brinquedo",
	"value": "200.00",
	"quantity": 20,
	"is_available": true,
	"image": null,
	"seller_id": 4
}

```
<h2> Atualização de produtos </h2>

Na rota products/:id/ o usuário sendo seller ou admin é capaz de editar e deletar produtos da aplicação
passando (o id dos produtos deve ser passado na url)   

```json
{
	"quantity": 50
}
```


`PATCH /products/:id - FORMA DA RESPOSTA - STATUS 200`

```json
{
	"id": 1,
	"name": "homem-aranha",
	"category": "brinquedo",
	"value": "200.00",
	"quantity": 50,
	"is_available": true,
	"image": null,
	"seller_id": 4
}
```

`DEL /products/:id - FORMA DA RESPOSTA - STATUS 204 no content`


em caso de erro na permissão:

```json
{
	"detail": "You do not have permission to perform this action."
}
```
<h2> Adicionar e Listar itens do Carrinho  </h2>

Nas rotas /carts/ e /carts/my_cart o usuário sendo cliente é capaz de adicionar produtos em seu carrinho
através da rota /carts/ e também podendo revisar e listar seus pedidos através da rota /carts/my_cart 
(o usuário precisa estar logado)   

```json{
	"product": 2,
	"product_quantity": 3
}
```
`POST /carts/ - FORMA DA RESPOSTA - STATUS 201 `


```json
{
	"id": 1,
	"cart": 1,
	"product_quantity": 3,
	"product": 2
}
```

`GET /carts/my_cart - FORMA DA RESPOSTA - STATUS 200 `

```json
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"cart": 1,
			"product_quantity": 3,
			"product": {
				"id": 2,
				"name": "caminhão",
				"category": "carrinho",
				"value": "120.00",
				"quantity": 10,
				"is_available": true,
				"image": null,
				"seller_id": 4
			}
		}
	]
}
```
<h2> Editar e Listar itens do Carrinho  </h2>

Nas rotas /carts/:id o usuário sendo cliente é capaz de editar e deletar produtos em seu carrinho
caso um vendedor tente editar/deletar itens do carrinho ele será impedido.

```json
{
	"product_quantity": 5
}
```

`PATCH /carts/:id - FORMA DA RESPOSTA - STATUS 200`

```json

{
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"cart": 1,
			"product_quantity": 5,
			"product": {
				"id": 2,
				"name": "caminhão",
				"category": "carrinho",
				"value": "120.00",
				"quantity": 10,
				"is_available": true,
				"image": null,
				"seller_id": 4
			
		}
	]
}

```

`DEL /carts/:id - FORMA DA RESPOSTA - STATUS 204 NO CONTENT`


em caso de erros:

```json
{
	"detail": "Not found."
}
```
```json
{
	"detail": "Authentication credentials were not provided."
}
```

<h2> Finalizar compras e listar pedidos</h2>

Na  rota /orders/ o usuário sendo cliente é capaz de finalizar os seus pedidos mantidos em seu carrinho,
no caso do vendedor ou admin ele poderá fazer atualizações e listar os pedidos que foram feitos pelo usuário na rota /orders/order_id,
/orders/finished/user_id, orders/sold/user_id.

`POST /orders/ - FORMA DA RESPOSTA - STATUS 201 `

```json
{
	"product": 1
}

```



```json
{
"id":1, 
"status":"Pedido Realizado", 
"created_at":"10/05/2023", 
"seller_id":1, 
"product":1, 
"user": [{
	"id":1,
	"first_name": "Pedro",
	"last_name": "Castro",
	"role": "Client",
	"email": "Pc@Gmail.com",
	"username": "PcGamerSP"
}]
}
```
`PATCH /orders/:id - FORMA DA RESPOSTA - STATUS 200 `


```json
{
"status": "Entregue"
}

```
```json
{
"id":1, 
"status":"Entregue", 
"created_at":"10/05/2023", 
"seller_id":1, 
"product":1, 
"user": [{
	"id":1,
	"first_name": "Pedro",
	"last_name": "Castro",
	"role": "Client",
	"email": "Pc@Gmail.com",
	"username": "PcGamerSP"
}]

```



`GET /orders/finished/:user_id - FORMA DA RESPOSTA - STATUS 200 `


```json
{
"id":1, 
"status":"Pedido Realizado", 
"created_at":"10/05/2023", 
"seller_id":1, 
"product":1, 
"user": [{
	"id":1,
	"first_name": "Pedro",
	"last_name": "Castro",
	"role": "Client",
	"email": "Pc@Gmail.com",
	"username": "PcGamerSP"
}]
```
`GET /orders/sold/:user_id - FORMA DA RESPOSTA - STATUS 200 `

```json{
"id":1, 
"status":"Entregue", 
"created_at":"10/05/2023", 
"seller_id":1, 
"product":1, 
"user": [{
	"id":1,
	"first_name": "Pedro",
	"last_name": "Castro",
	"role": "Client",
	"email": "Pc@Gmail.com",
	"username": "PcGamerSP"
}]
```

em caso de erros na resposta :

```json
{
	"detail": "Not found."
}
```
```json
{
	"detail": "Authentication credentials were not provided."
}
```






