<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Untitled Document</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>

<body>
<form name="form1" action="" method="post" enctype="multipart/form-data" class="wrapper" >
    <table>
        <tr>
            <td><h1 style="color: whitesmoke;">Select file</h1></td>
            <td><input type="file" name="f1"></td>
        </tr>
        <tr>
            <td><input class="btn" type="submit" name="submit1" value="upload"></td>
            
        </tr>
    </table>
</form>
<style>
        body {
            background: url('Landing_Page.png') no-repeat center center fixed; 
            background-size: cover;
            height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .wrapper {
            width: 420px;
            background: transparent;
            border:2px solid rgba(255, 255, 255, .2);
            backdrop-filter:blur(20px);
            box-shadow: 0 0 10px rgba(0 , 0 , 0 , .2);
            color: #fff;
            border-radius: 10px;
            padding: 30px 40px;
            position: relative;
            top: 2%;
            left: 15%;

        }

        .wrapper h1{
            font-size: 36px;
            text-align: center;
            color: gainsboro;
        }
        .wrapper .input-box {
            position: relative;
            width: 100%;
            height: 50px;
            margin: 30px 0;
        }

        .input-box input{
            width: 100%;
            height: 100%;
            background: transparent;
            border: none;
            outline: none;
            border: 2px solid rgba(0, 255, 255, .2);
            border-radius: 40px;
            font-size: 16px;
            color: #fff;
            padding: 20px 45px 20px 20px;
        }
        .input-box input::placeholder{
            color: #fff;
        }
        .input-box i{
            position: absolute;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 20px;

        }

        .wrapper .btn{
            width: 100%;
            height: 45px;
            border-radius: 40px;
            border: none;
            outline: none;
            background: #fff;
            box-shadow: 0 0 10px rgba(0 , 0 , 0 , .1);
            cursor: pointer;
            font-size: 16px;
            color: #333;
            font-weight: 600;
        }

        form {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
            position: absolute;
            top:50px;
            left:50px;
        }

        label {
            font-size: 18px;
            font-weight: bold;
        }

        textarea {
            width: 100%;
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }

        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
    </style>

<?php
$conn = new mysqli("localhost", "root", "", "test_blob1");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if(isset($_POST["submit1"])) {
    $stmt = $conn->prepare("INSERT INTO table1 (image) VALUES (?)");
    $stmt->bind_param("s", $image);

    $image = file_get_contents($_FILES['f1']['tmp_name']);
    $stmt->execute();

    $stmt->close();
}

if(isset($_POST["submit2"])) {
    $res = $conn->query("SELECT * FROM table1");
    echo "<table>";
    echo "<tr>";
    
    while($row = $res->fetch_assoc()) {
        echo "<td>"; 
        echo '<img src="data:image/jpeg;base64,'.base64_encode($row['image']).'" height="200" width="200"/>';
        echo "<br>";
        ?><a href="delete.php?id=<?php echo $row["id"]; ?>">Delete</a> <?php
        echo "</td>";
    }
    
    echo "</tr>";
    echo "</table>";
}

$conn->close();
include('retrieve.php');
?>

</body>
</html>
