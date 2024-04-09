import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um valor menor que 100: ");
        int numero = scanner.nextInt();

        if (numero >= 100) {
            System.out.println("O número inserido não é menor que 100");
        } else {
            int dezena = numero / 10;
            int unidade = numero % 10;
            int somaDigitos = dezena + unidade;
            System.out.println(somaDigitos);
        }
    }
}

