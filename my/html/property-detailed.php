<?php
#$conn = new mysqli("localhost", "root", "minimoto", "photoboot");
$conn = new mysqli("159.203.136.91", "photoboot1", "minimoto", "photoboot");
$coin = 0;
$costo = 2;
$redis = new Redis();
// Check connection
if ($conn->connect_error) {
  die("Connection Database failed: " . $conn->connect_error);
} 

$sql = "SELECT id, coin, crediti, nome, gettoni FROM crediti WHERE ID ='1'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  $redis->connect("127.0.0.1", 6379);
    // output data of each row
    while($row = $result->fetch_assoc()) {
      
      

      $redis->set("id", $row["id"]);
      $redis->set("coin", $row["coin"]);
      $redis->set("crediti", $row["crediti"]);
      $redis->set("gettoni", $row["gettoni"]);
      $redis->set("nome", $row["nome"]);

      $id= $redis->get("id");
      $coin= $redis->get("coin");
      $crediti= $redis->get("crediti");
      $gettoni= $redis->get("gettoni");

      #die("id" . $id."       coin"  .$coin."       crediti". $crediti."       gettoni". $gettoni);




    }
  } else {
    echo "0 results";
  
}
?>




<div class="container" >


















  <?php if ($crediti < 1 AND $gettoni >0):?>
  <!-- Trigger the modal with a button -->

  <!-- Modal -->
    <div class="modal show" id="myModal" role="dialog">
    
      <!-- Modal content-->

        <div class="modal-body">
            <p class="my"></p>
            <p class="my"></p>
            <i class="my">#Photoboot <?php echo $id; ?></i>
            <p class="my"> .</p>
            <p class="my">. </p>
            <p class="my">. </p>
            <p class="my">. </p>
            <p class="my">. </p>
            <p class="my">. </p>


            <p class="blink" >Insere monete</p>
            <p class="my">. </p>

            <p class="my">Inseriti <?php echo $coin; ?>/<?php echo $costo; ?>€</p>
        </div>

      
    </div>
    
    <?php endif; ?>


    <?php if ($gettoni < 1 ):?>
  <!-- Trigger the modal with a button -->

  <!-- Modal -->
    <div class="modal show" id="myModal" role="dialog">
    
      <!-- Modal content-->

        <div class="modal-body">
            <p class="my">.</p>
            <p class="my">.</p>
            <p class="my">.</p>
            <i class="my">#Photoboot  ID:<?php echo $id; ?></i>
            <p class="my">.</p>
            <p class="my">.</p>
            <p class="blink" >################</p>
            <p class="my">################### </p>
            <p class="my"></p>
            <p class="my"></p>

            <p class="my"> GETTONI ESAURITI CONTATTARE GESTORE</p>
            <p class="my"></p>
            <p class="my">################### </p>
            <p class="blink" >################</p>

            <i class="my">#PhotobootByValex</i>



        </div>

      
    </div>
    
    <?php endif; ?>















  




<div>