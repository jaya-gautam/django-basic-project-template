# Django project-ready setup (from a minimal Ubuntu 12.04 box)

Vagrant.configure("2") do |config|
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.network :forwarded_port, guest: 5432, host: 15432
  config.vm.network :forwarded_port, guest: 8000, host: 18000
  # is forwarded by default on newer Vagrant (at least on 1.2.x)
  #config.vm.network :forwarded_port, guest: 22, host: 2222

  config.vm.synced_folder ".", "/home/vagrant/projects/{{ project_name }}"

  # args: $1 - project name, $2 - database/user name (optional, defaults to $1)
  config.vm.provision :shell, :path => "Vagrantfile.provision/provision.sh", :args => "{{ project_name }}"
end
