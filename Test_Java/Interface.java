import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.Scanner;

public class Interface {
  public static void main(String[] args) {
    Toy[] t = new Toy[3];
    t[0] = new Toy(1, "bear", 2.0);
    t[1] = new Toy(2, "car", 3.5);
    t[2] = new Toy(3, "doll", 5.0);

    PriorityQueue<Toy> queue = new PriorityQueue<>(Comparator.comparingDouble(Toy::getWeight));
    for (Toy toy : t) {
      queue.add(toy);
    }
    PriorityQueue<Toy> totalQueue = new PriorityQueue<>(Comparator.comparingDouble(Toy::getWeight));
    totalQueue.addAll(queue);

    Scanner sc = new Scanner(System.in);
    System.out.println("приветствуем тебя в лотерее");
    System.out.println("введите 1 если готовы играть");
    System.out.println("нажмите любую кнопку для выхода");
    String choise = sc.next();

    if (choise.equals("1")) {
      try (
          PrintWriter writer = new PrintWriter(new FileWriter("Test_Java\\win_list.txt"))) {

        for (int i = 0; i < 30; i++) {
          Toy toy = totalQueue.poll();
          int rnd_percent = new Random().nextInt(100);

          if (toy.getId() == 1) {
            if (rnd_percent <= 20) {
              writer.printf(" %d. %s (%.2f)n ", toy.getId(), toy.getName(), toy.getWeight());
            } else {
              System.out.println("miss");
            }
          }

          if (toy.getId() == 2) {
            if (rnd_percent <= 35) {
              writer.printf(" %d. %s (%.2f)n ", toy.getId(), toy.getName(), toy.getWeight());
            } else {
              System.out.println("miss");
            }
          }

          if (toy.getId() == 3) {
            if (rnd_percent <= 50) {
              writer.printf(" %d. %s (%.2f)n ", toy.getId(), toy.getName(), toy.getWeight());
            } else {
              System.out.println("miss");
            }
          }

          if (totalQueue.peek() == null) {
            totalQueue.addAll(queue);
          }

        }
      } catch (IOException ex) {
        System.err.println("Error writing to file: " + ex.getMessage());
      }
    } else {
      System.out.println("Выход");
    }

  }
}
