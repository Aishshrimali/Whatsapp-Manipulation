<?php
$conn = mysqli_connect("localhost","root","","wp");
	if(!$conn){
		mysqli_connect_error();
	}	
	if(isset($_GET['sent'])){
		$name= $_GET['sent']; 
		if($name == 'sent'){
			$sql ="SELECT * FROM `msg` WHERE `update`!= '$name' ORDER BY `id` DESC";
			$sql = mysqli_query($conn,$sql);
			$data = mysqli_fetch_assoc($sql);
			$id = $data['id'];
			$update = mysqli_query($conn, "UPDATE `msg` SET`update`= '$name' WHERE `id`='$id'");
			if($update){
				echo $data['msg'];
				echo $data['contact'];
			
			}
		}	
			
		
	}
?>