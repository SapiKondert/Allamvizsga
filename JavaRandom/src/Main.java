import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random rand = new Random();
        String filePath = "output.txt";
        String content = "Hello, this is a sample text written to the file!";
        try {
            FileWriter fileWriter = new FileWriter(filePath);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            for (int i=0;i<2000000;i++){
                int rand_int1 = rand.nextInt(2);
                bufferedWriter.write(""+rand_int1);

            }
            bufferedWriter.close();
            System.out.println("File written successfully!");
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file.");
            e.printStackTrace();
        }
    }
}