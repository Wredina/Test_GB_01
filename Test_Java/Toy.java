import java.util.PriorityQueue;

public class Toy {
  int id;
  String name;
  double weight;

  public Toy(int id, String name, double weight) {
    this.id = id;
    this.name = name;
    this.weight = weight;
  }

  public int getId() {
    return id;
  }

  public String getName() {
    return name;
  }

  public double getWeight() {
    return weight;
  }

  public void add(PriorityQueue<Toy> new_toy) {
  }

  public Object peek() {
    return null;
  }

  public void addAll(PriorityQueue<Toy> new_toy) {
  }
}
