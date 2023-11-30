<?php

require 'connection.php';

// Query the database to get the latest image
$sql = "SELECT image FROM table1 ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);

// Check if there are results
if ($result) {
    if ($result->num_rows > 0) {
        // Fetch the row
        $row = $result->fetch_assoc();

        // Get the image binary data
        $imageData = $row['image'];

        
        // Create a new image file
        $imageFilePath = 'C:/xampp/htdocs/blob1/images/images.jpg';
        $imageFileStream = fopen($imageFilePath, 'wb'); // 'wb' means write binary

        // Check if file stream is opened successfully
        if ($imageFileStream) {
            // Write binary data to the image file
            fwrite($imageFileStream, $imageData);

            // Close the file stream
            fclose($imageFileStream);

            echo "Image successfully written to $imageFilePath";
        } else {
            echo 'Error opening the image file for writing.';
        }
    } else {
        echo "No results found";
    }
} else {
    echo "Query failed: " . $conn->error;
}
$pythonScript = "encrypt.py";

// Use shell_exec to run the Python script
$output = shell_exec("python $pythonScript");

// Close the database connection
$conn->close();

?>
