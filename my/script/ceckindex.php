<?php
#$conn = new mysqli("localhost", "root", "minimoto", "photoboot");
$conn = new mysqli("159.203.136.91", "photoboot1", "minimoto", "photoboot");

$coin = 0;
$costo = 2;

// Check connection
if ($conn->connect_error) {
  die("Connection Database failed: " . $conn->connect_error);
} 

$sql = "SELECT id, coin, crediti, nome, gettoni FROM crediti WHERE ID ='1'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
      $coin= $row["coin"];
      $id= $row["id"];
      $crediti= $row["crediti"];
      $gettoni= $row["gettoni"];
    }
  } else {
    echo "0 results";
  
}
?>


<div class="container" >






    <?php if ($crediti < 1 ):?>
  <!-- Trigger the modal with a button -->

  <!-- Modal -->
    <div class="modal show" id="myModal" role="dialog">
    
      <!-- Modal content-->

        <div class="modal__body">
            <p class="modal__body"></p>
            <p class="modal__body"></p>
            <p class="modal__body"></p>
            <i class="modal__body">#Photoboot <?php echo $id; ?></i>
            <p class="modal__body"></p>
            <p class="modal__body"></p>
            <p class="blink" >Gettoni <?php echo $gettoni; ?></p>
            <p class="blink" >Insere monete</p>
            <p class="modal__body">Inseriti <?php echo $coin; ?>/<?php echo $costo; ?>€</p>
        </div>

      
    </div>
    
    <?php endif; ?>


    <?php if ($gettoni < 1 ):?>
  <!-- Trigger the modal with a button -->

  <!-- Modal -->
    <div class="modal show" id="myModal" role="dialog">
    
      <!-- Modal content-->

        <div class="modal__body">
            <p class="modal__body"></p>
            <p class="modal__body"></p>
            <p class="modal__body"></p>
            <i class="modal__body">#Photoboot <?php echo $id; ?></i>
            <p class="modal__body"></p>
            <p class="modal__body"></p>
            <p class="blink" >################</p>
            <p class="modal__body">################### </p>
            <p class="modal__body"></p>
            <p class="modal__body"></p>

            <p class="modal__body"> GETTONI ESAURITI CONTATTARE GESTORE</p>
            <p class="modal__body"></p>
            <p class="modal__body">################### </p>
            <p class="blink" >################</p>
            <p class="modal__body"><?php echo $id; ?></p>

            <i class="modal__body">#PhotobootByValex</i>



        </div>

      
    </div>
    
    <?php endif; ?>

</div>