import java.lang.reflect.Array;
import java.util.List;
import java.util.*;

public class userGroup{
    public static void main(String[] args) {


        List<String> grpNames = Arrays.asList("bronze", "gold", "silver", "diamond", "platinum", "copper", "nickel", "titanium", "iron", "cobalt", "tungsten", "mercury");

        //Empty list to store names from user table
        List<String> names = Arrays.asList("Aaron", "Ethan", "green", "Hassan", "Isidro", "Jason", "Jesus", "Jose", "Karen", "Manduul", "Muhammad", "Nathan", "Omar", "Riley", "Sergey", "Stuart", "Tom", "yellow");

        int guid = 1000;
        System.out.println(grpNames);
        System.out.println(names);

        //Add 4 users in 4 different groups
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                
                System.out.println("i = " +i);
                System.out.println("j = "+j);
                
                String sql = "("; 
                sql = sql + guid++ + ",";
                sql = sql + "'" + names.get(i) + "','";
                sql = sql + grpNames.get(j) + "',";
                sql = sql + "'doesnt matter',";
                sql = sql + "0,false)";
                
                //Remove used names from the names list
                
                System.out.println(sql);
                
                
            }    
        }
    }
}
