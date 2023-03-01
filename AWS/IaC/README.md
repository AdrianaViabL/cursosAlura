# Dicas

esteja logado tanto no terraform como no aws localmente para que essa aplicação funcione
obs: tenha certeza que a chave do aws está ativa (dentro do IAM > Credenciais de segurança)

```
terraform init
```

deve ser configurado uma chave SSH (no AWS ela é gerada, dentro do 'Conectar-se à instância' ao clicar no 'conectar' 
estando dentro do EC2 e deve clicar na opção Cliente SSH) para que a maquina consiga executar no AWS


## Comandos via terminal:

para ler as configurações de montagem da maquina virtual
```
terraform plan
```

para aplicar as configurações que estão no main.tf
```
terraform apply
```

## Conectando a instancia criada dentro do AWS
Obs.: isso deve ser feito apos a instancia ter sido criada com a ajuda do terraform com o comando 'terraform apply'


No AWS, na area do 'Painel EC2' acesse as 'Instâncias (em execução)', selecione a instancia e clique no botão 'conectar',
copie o comando de exemplo na aba 'Cliente SSH' e execute no terminal


## Usando o Ansible

Depois de ter configurado o hosts.yml (com o ip da instancia no aws) e o playbook.yml (com os comandos que serão executados na alteração dessa instancia), 
entre no terminal e digite:
Obs.: o ansible nao funciona diretamente no windows, um aluno da Alura ajudou nessa parte ao disponibilizar dois videos
https://www.youtube.com/watch?v=tX-PPvDAtKo - Como instalar o Ubuntu como subsistema do Windows e instalar o Ansible
https://www.youtube.com/watch?v=L_xReF3_iCE - Como usar o Ansible em um subsistema Linux do Windows (como instalar na descrição)

```
ansible-playbook playbook.yml -u ubuntu --private-key iac-teste.pem -i hosts.yml
```
