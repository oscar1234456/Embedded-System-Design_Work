<?php/**\mainpage   網頁控制七段顯示器
*  - \subpage 名稱：7seg.php
*  - \subpage 作者：110616038 陳泰元
*  - \subpage 版本：1.0
*  - \subpage 日期：2020/5/9
*  操作說明：
*  按下網頁的按鈕，7段顯示器為顯示出與按鈕相同之數字。
*  另外在網頁中增加圖示，表示出目前應該顯示的數字。
*  軟硬設備:
*  pi4
*  apache2 + php7 (cli)
*  work link: https://youtu.be/8cZEMgK5oew
*/ ?>
<html>
<head><title>7segment display</title></head>
<style>
		.search{
            border-radius: 4px;
            padding: 16px;
            font-size: 20px;
            width : 50px;
            height: 50px;
        }
</style>
<body>

<?php 
	$icon = -1;
	if($_POST["LAMP"] != null){
		if (strcmp( $_POST [ "LAMP" ], "1" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 1" ); //利用參數呼叫
			$icon = 1;
			sleep(0.05);
		}
		
		if (strcmp( $_POST [ "LAMP" ], "2" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 2" );
			$icon = 2;
			sleep(0.05);
		}
		if (strcmp( $_POST [ "LAMP" ], "3" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 3" );
			$icon = 3;
			sleep(0.05);
		}
		
		if (strcmp( $_POST [ "LAMP" ], "4" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 4" );
			$icon = 4;
			sleep(0.05);
		}
		if (strcmp( $_POST [ "LAMP" ], "5" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 5" );
			$icon = 5;
			sleep(0.05);
		}
		
		if (strcmp( $_POST [ "LAMP" ], "6" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 6" );
			$icon = 6;
			sleep(0.05);
		}
		if (strcmp( $_POST [ "LAMP" ], "7" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 7" );
			$icon = 7;
			sleep(0.05);
		}
		
		if (strcmp( $_POST [ "LAMP" ], "8" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 8" );
			$icon = 8;
			sleep(0.05);
		}
		if (strcmp( $_POST [ "LAMP" ], "9" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 9" );
			$icon = 9;
			sleep(0.05);
		}
		
		if (strcmp( $_POST [ "LAMP" ], "0" ) == 0) {
			shell_exec( "sudo python3 7seg_input.py 0" );
			$icon = 0;
			sleep(0.05);
		}
	}
?>

<h1> 7Segment display Control</h1>
<form action="7seg.php" method="post">
	<table>
        <tr>
            <td> <input type="submit" name="LAMP" value="7" class="search" ></td>
            <td> <input type="submit" name="LAMP" value="8" class="search"></td>
            <td> <input type="submit" name="LAMP" value="9" class="search"></td>
        </tr>
        <tr>
            <td> <input type="submit" name="LAMP" value="4" class="search"></td>
            <td> <input type="submit" name="LAMP" value="5" class="search"></td>
            <td> <input type="submit" name="LAMP" value="6" class="search"></td>
        </tr>
        <tr>
            <td> <input type="submit" name="LAMP" value="1" class="search"></td>
            <td> <input type="submit" name="LAMP" value="2" class="search"></td>
            <td> <input type="submit" name="LAMP" value="3" class="search"></td>
			<td> <input type="submit" name="LAMP" value="0" class="search"></td>
    </table>
	<br>
	<?php 
		if($icon != -1){?>
		<img src="img/<?php print($icon).".png"; ?>" width = "200" height = "300"alt="">
    <?php }
	?>
</form>





</body>
</html>