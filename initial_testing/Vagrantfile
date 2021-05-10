Vagrant.configure("2") do |config|

    config.vm.box = "ubuntu/bionic64"   # Ubuntu 18.04 (use focal64 for 20.04)
  
    config.vm.provider "virtualbox" do |vb|
    #   # Display the VirtualBox GUI when booting the machine
       vb.gui = false
    #
    #   # Customize the amount of memory on the VM:
       vb.memory = "2048"
    end
  
    config.vm.provision "shell", path: "bootstrap.sh"
  
    config.vm.provision "file", source: "C:/Courses/Cloud/a_key.pem", destination: "~/.ssh/"
  
    # let's also copy our ansible.cfg, MyInventory and cloud.yaml file
    config.vm.provision "file", source: "C:/Courses/Cloud/4287-PA3/.ansible.cfg", destination: "~/.ansible.cfg"
    config.vm.provision "file", source: "C:/Courses/Cloud/4287-PA3/MyInventory", destination: "~/.ansible/MyInventory"
    config.vm.provision "file", source: "C:/Courses/Cloud/4287-PA3/clouds.yaml", destination: "~/.config/openstack/clouds.yaml"
  
    config.vm.provision "file", source: "C:/Courses/Cloud/4287-PA3/consumer.py", destination: "~/consumer.py"
    config.vm.provision "file", source: "C:/Courses/Cloud/4287-PA3/daemon.json", destination: "~/daemon.json"
    config.vm.provision "file", source: "C:/Courses/Cloud/4287-PA3/tasks/local.ini", destination: "~/local.ini"
   
    $script = <<-SCRIPT
       chmod go-rwx ~/.ssh/a_key.pem
    SCRIPT
    config.vm.provision "shell", inline: $script, privileged: false
  
    config.vm.synced_folder "C:/Courses/Cloud/4287-PA3", "/vagrant"
  
    config.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "playbook_master.yml"
      ansible.galaxy_role_file = "collection.yaml"
      ansible.galaxy_command = "ansible-galaxy collection install -r %{role_file} --force"
      ansible.verbose = true
      ansible.install = true  # installs ansible (and hence python on VM)
      ansible.limit = "all"
      ansible.inventory_path = "MyInventory"  # inventory file
    end
  
  end
  