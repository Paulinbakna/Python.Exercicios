import csv

def leitor_csv(caminho):
    data = []
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            csv_reader = csv.reader(arquivo)
            header = next(csv_reader)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f'O arquivo -->> {caminho} <<-- não foi encontrado!')            
    except Exception as e:
        print(f'Ocorreu um erro ao ler o arquivo: -->> {e}')
        
    return header, data

def media_dos_valores(data,coluna):
    try:
        values = [float(row[coluna]) for row in data if row[coluna]]
        
        media = sum(values) / len(values)
    
    except ZeroDivisionError:
        print('Divisão por zero ao calcular a média (nenhum dado na coluna).')
        media = None
    
    except ValueError:
        print("Erro ao converter os valores para float.")
        media = None
        
    return media

def novo_arquivo(novo_arquivo, header, data):
    try:
        with open(novo_arquivo, mode='w',encoding='utf-8', newline='') as arquivo:
            csv_writer = csv.writer(arquivo)
            csv_writer.writerow(header)
            csv_writer.writerows(data)
    except Exception as e:
        print(f'Ocorreu um erro ao escrever o arquivo: {e}')

def main():
    input_file = r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Projeto Prático\dados.csv'
    output_file = r'C:\Users\Paulin\Documents\GitHub\Python.Exercicios\Projeto Prático\resultado.csv'
    
    header, data = leitor_csv(input_file)
    
    if not data:
        print('Nenhum dado foi lido do arquivo')
        return

    try:
        column_index = header.index('   idade')
    except ValueError:
        print('Coluna "idade" não encontrada no arquivo csv')
        return
        
    media = media_dos_valores(data,column_index)
    
    if media is not None:
        header.append('Média idade')
        for row in data:
            row.append(f' {media}')
        
        novo_arquivo(output_file, header, data)
        print(f'Resultados foram escritos em -->> {output_file} <<--')

if __name__ == "__main__":
    main()
