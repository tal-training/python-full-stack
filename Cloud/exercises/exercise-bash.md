 Here are some common Bash commands with brief explanations, demonstrations, and exercises for beginners:

0. To see your Linux distribution:

`uname -a`

1. `cd`: Change Directory

Demonstration:
```bash
# Switch to the parent directory
$ cd ..

# Switch to the previous directory
$ cd ~

# Switch to a specific directory
$ cd /path/to/directory
```
Exercise: Navigate through different directories using `cd`. Try switching to your home directory (`~`), the parent directory (`..`), and a specific directory (/path/to/directory).

2. `ls`: List Files and Directories

Demonstration:
```bash
# List files and directories in the current directory
$ ls

# List files and directories in a specific directory
$ ls /path/to/directory
```
Exercise: Run `ls` to see the files and directories in your current directory. Also, try running `ls` with different options (-l, -a, etc.) to view different types of information.

3. `mkdir`: Make a Directory

Demonstration:
```bash
# Create a new directory
$ mkdir my_new_directory

# Create a new directory with a specific name and path
$ mkdir /path/to/my_new_directory
```
Exercise: Create a few new directories using `mkdir`. Try creating a directory with a simple name, and then try creating one with a more complex name and path.

4. `rm`: Remove File or Directory

Demonstration:
```bash
# Remove a file
$ rm example.txt

# Remove a directory
$ rm -r my_directory
```
Exercise: Remove a few files and directories using `rm`. Be careful when removing directories, as this command will permanently delete everything inside the directory without prompting for confirmation.

5. `touch`: Create a New Empty File

Demonstration:
```bash
# Create a new empty file
$ touch my_new_file.txt
```
Exercise: Create a few new empty files using `touch`. Give them different names and extensions.

6. `echo`: Output Text to a File or the Terminal

Demonstration:
```bash
# Output text to the terminal
$ echo "Hello World!"

# Output text to a file
$ echo "Hello World!" > my_file.txt
```
Exercise: Use `echo` to output some text to the terminal and to a file. Try adding different types of content, such as variables and special characters.

7. `cat`: Concatenate and Display Files

Demonstration:
```bash
# Display the contents of a file
$ cat my_file.txt

# Display the contents of multiple files
$ cat my_file1.txt my_file2.txt
```
Exercise: Use `cat` to display the contents of a few files. Try combining multiple files into a single output stream.

8. `nano`: Text Editor

Demonstration:
```bash
# Open a file in nano editor
$ nano my_file.txt

# Edit the contents of a file
$ nano my_file.txt
```
Exercise: Open a file in nano and edit its contents. Save the changes and exit the editor.

9. `pwd`: Print Working Directory

Demonstration:
```bash
# Print the current working directory
$ pwd
```
Exercise: Run `pwd` to print the current working directory. Try navigating to different directories and running `pwd` again to see the updated directory path.

10. `man`: Manual Pages

Demonstration:
```bash
# View the manual page for the ls command
$ man ls
```
Exercise: Look up the manual page for a few different commands, such as `cd`, `mkdir`, and `echo`. Read through the documentation to learn more about each command's usage and options.

These are just a few basic Bash commands to get you started. There are many more commands available, and you can continue exploring and learning as you become more comfortable with the command line interface.

 Here are some basic commands for working with packages on Debian-based distributions (such as Ubuntu) using the `apt` command, and on Red Hat-based distributions (such as CentOS) using the `yum` command:

Apt Commands:

1. `apt update`: Update the package index
	* Example: `sudo apt update`
2. `apt upgrade`: Upgrade all installed packages to the latest version
	* Example: `sudo apt upgrade`
3. `apt install <package>`: Install a new package
	* Example: `sudo apt install firefox`
4. `apt remove <package>`: Remove a package
	* Example: `sudo apt remove firefox`
5. `apt purge <package>`: Remove a package and its configuration files
	* Example: `sudo apt purge firefox`
6. `apt search <keyword>`: Search for packages containing a keyword
	* Example: `sudo apt search firefox`
7. `apt show <package>`: Show detailed information about a package
	* Example: `sudo apt show firefox`
8. `apt policy <package>`: Show the installation policy for a package
	* Example: `sudo apt policy firefox`

Yum Commands:

1. `yum update`: Update the package index
	* Example: `sudo yum update`
2. `yum upgrade`: Upgrade all installed packages to the latest version
	* Example: `sudo yum upgrade`
3. `yum install <package>`: Install a new package
	* Example: `sudo yum install firefox`
4. `yum remove <package>`: Remove a package
	* Example: `sudo yum remove firefox`
5. `yum erase <package>`: Remove a package and its configuration files
	* Example: `sudo yum erase firefox`
6. `yum search <keyword>`: Search for packages containing a keyword
	* Example: `sudo yum search firefox`
7. `yum info <package>`: Show detailed information about a package
	* Example: `sudo yum info firefox`
8. `yum provides <package>`: Show the packages that provide a particular package
	* Example: `sudo yum provides firefox`

Note: In order to use the `yum` command, you need to have the `yum` package installed on your system. You can install it by running the following command: `sudo apt install yum` (on Debian-based distributions) or `sudo yum install yum` (on Red Hat-based distributions).

Again, these are just some basic examples, and there are many more options and flags that you can use with these commands to customize their behavior. It's always a good idea to consult the documentation for the specific command you're interested in to learn more about its usage and options.