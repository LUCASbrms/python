alunos = []
# Loop principal do programa
while True:
    print("Selecione uma opção:")
    print("1. Criar aluno")
    print("2. Ler alunos")
    print("3. Buscar aluno por ID")
    print("4. Atualizar aluno")
    print("5. Excluir aluno")
    print("0. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1": # Cadastro do aluno
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Difite a idade do aluno: "))
        
        if len(alunos) == 0:
            id_aluno = 1
        else: 
            id_aluno = alunos[-1][0] + 1
            
        dados_aluno = [id_aluno, nome, idade]
        alunos.append(dados_aluno)
        
        print("Aluno criado com sucesso. ")
        print(alunos)

    elif opcao == "2": # Consultar aluno
        id_busca = int(input("Digite o ID do aluno que deseja consultar: "))
        encontrado = False
        for aluno in alunos:
            if aluno[0] == id_busca:
                print("ID:", aluno[0])
                print("Nome:", aluno[1])
                print("Idade:", aluno[2])
                encontrado = True
                break

    elif opcao == "3": #Busca aluno por ID
        id_busca = int(input("Digite o ID do aluno que deseja buscar"))
        encontrado = False
        for aluno in alunos:
            if aluno[0] == id_busca:
                print("ID: ", aluno[0])
                print("Nome: ", aluno[1])
                print("Idade: ", aluno[2])
                encontrado = True
                break
        if not encontrado:
            print("Aluno não encontrado. ")

    elif opcao == "4": # Atualiza por ID
        def atualiza_aluno():
    # pega as informacoes do usuario e valida elas
            while True:
                try:
                    # remove qualquer espaço em branco antes ou depois do input do usuario:
                    id_busca = int(input('Qual o ID deseja atualizar? ').strip())
                    if id_busca > 0:
                        break # se deu tudo certo sai do loop e vai pro for in na lista de alunos
                    else:
                        print('O ID começa em 1')
                # trata algum eventual erro
                except:
                    print('ID deve ser um número inteiro válido maior que 0. Tente novamente')
            
            encontrado = False # variavel que controla se o ID foi encontrado & atualizado ou nao
            # pra cada aluno na lista de alunos:
            for aluno in alunos:
                if aluno[0] == id_busca: # se o ID passado pelo usuário for encontrado na lista entra na validação e depois pra atualização
                    while True:
                        try:
                            # pega os dados do usuario                limpa qualquer espaço em branco
                            novo_nome = str(input('Qual o novo nome do aluno? ')).strip() # input do usuario
                            nova_idade = int(input(('Qual a nova idade do aluno? ')).strip()) # input do usuario

                            # checa se os dados são válidos
                            if novo_nome and nova_idade > 0: # se o nome for passado e a idade for positiva:
                                break # quebra do loop e vai pra atualização dos dados
                            else:
                                print('Idade não pode ser menor que 0 e nome não pode ficar vazio') 
                                continue # volta pro começo do loop
                        except:
                            print('Nome deve conter apenas caracteres válidos e idade deve ser um número inteiro maior que 0') # caso alguma coisa no try der errada, cai aqui e volta pro começo do loop

                    # ---- Atualização dos dados do Aluno ----- #            
                    aluno[0] = id_busca # atualiza o id do aluno escolhido
                    aluno[1] = novo_nome # atualiza o nome do aluno
                    aluno[2] = nova_idade # atualiza a idade do aluno
                    print('Aluno atualizado com sucesso!')
                    encontrado = True
                    break # quebra o loop e termina a função
                
        # --- Caso o aluno (ID) não for encontrado
        if not encontrado:
            print('Aluno não encontrado')
            


        atualiza_aluno() # chama a função pra ser executada
        print(alunos) # printa a nova lista de alunos atualizada

    elif opcao == "5": # Excluir Aluno
        id_busca = int(input("Digite o ID do aluno que deseja excluir: "))
        encontrado = False
        for aluno in alunos:
            if aluno[0] == id_busca:
                alunos.remove(aluno)
                print("Aluno excluído com sucesso.")
                encontrado = True
                break

    elif opcao == "0": # SAIR DO PROGRAMA
        break

    else:
        print("Opção inválida. Por favor, digite novamente.")