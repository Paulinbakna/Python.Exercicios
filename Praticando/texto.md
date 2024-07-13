def main():
    input_file = 'dados.csv'
    output_file = 'resultados.csv'
    
    # Passo 1: Ler dados do arquivo CSV
    header, data = leitor_csv(input_file)
    
    if not data:
        print("Nenhum dado foi lido do arquivo.")
        return
    
    # Adicionando uma nova coluna para a média
    column_index = 1  # Índice da coluna que queremos analisar
    average = media_dos_valores(data, column_index)
    
    if average is not None:
        header.append('Média')
        for row in data:
            row.append(average)
    
    # Passo 3: Escrever resultados no novo arquivo CSV
    novo_arquivo(output_file, header, data)
    
    print(f"Resultados foram escritos em {output_file}")

if __name__ == "__main__":
    main()
