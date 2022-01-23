from model import *

muhammed = Person(1, "Muhammed Said Kaya", "Platform")

people = [
  muhammed
]

vcs = TechnologyStack(1, "Version Control Systems")
pl = TechnologyStack(2, "Programming Languaes")
frameworks = TechnologyStack(3, "Frameworks and Libraries")
db = TechnologyStack(4, "SQL/NoSQL Databases")
iac = TechnologyStack(5, "IaC")
k8s = TechnologyStack(6, "Container Orchestration Systems")
monitoring = TechnologyStack(7, "Monitoring")
logging = TechnologyStack(8, "Log Management")
secrets =   TechnologyStack(9, "Secret Management")
mesh = TechnologyStack(10, "Service Mesh")
automation = TechnologyStack(11, "Automation Server")
cloud = TechnologyStack(12, "Cloud Providers")

technology_stack_values = [
  vcs, pl, frameworks, db, iac, k8s, monitoring, logging, secrets, mesh, automation, cloud
]

git = Technology(1, "Git", 1)
python = Technology(2, "Python", 2)
java = Technology(3, "Java", 2)
js = Technology(4, "JavaScript", 2)
spring = Technology(5, "Spring", 3)
react = Technology(6, "React", 3)
postgres = Technology(7, "PostgreSQL", 4)
mysql = Technology(8, "MySQL", 4)
mongo = Technology(9, "MongoDB", 4)
packer = Technology(10, "Packer", 5)
terraform = Technology(11, "Terraform", 5)
ansible = Technology(12, "Ansible", 5)
pulumi = Technology(13, "Pulumi", 5)
docker = Technology(14, "Docker", 6)
k8s = Technology(15, "Kubernetes", 6)
rancher = Technology(16, "Rancher", 6)
prometheus = Technology(17, "Prometheus", 7)
grafana = Technology(18, "Grafana", 7)
instana = Technology(19, "Instana", 7)
elk_stack = Technology(20, "ELK Stack", 8)
humio = Technology(21, "Humio", 8)
hashicorp_vault = Technology(22, "Vault", 9)
istio = Technology(23, "Istio Service Mesh", 10)
jenkins = Technology(24, "Jenkins", 11)
gitlab_ci = Technology(25, "Gitlab CI", 11)
aws = Technology(26, "AWS", 12)

technologies = [
  git, 
  python, java, js, spring, react, 
  postgres, mysql, mongo, 
  packer, terraform, ansible, pulumi, 
  docker, k8s, rancher, 
  prometheus, grafana, instana,
  elk_stack, humio,
  hashicorp_vault,
  istio,
  jenkins, gitlab_ci,
  aws
]

knowledges = [
  Knowledge(1, p_id=1, t_id=1),
  Knowledge(2, p_id=1, t_id=2),
  Knowledge(3, p_id=1, t_id=3),
  Knowledge(4, p_id=1, t_id=4),
  Knowledge(5, p_id=1, t_id=5),
  Knowledge(6, p_id=1, t_id=6),
  Knowledge(7, p_id=1, t_id=7),
  Knowledge(8, p_id=1, t_id=8),
  Knowledge(9, p_id=1, t_id=9),
  Knowledge(10, p_id=1, t_id=10),
  Knowledge(11, p_id=1, t_id=11),
  Knowledge(12, p_id=1, t_id=12),
  Knowledge(13, p_id=1, t_id=13),
  Knowledge(14, p_id=1, t_id=14),
  Knowledge(15, p_id=1, t_id=15),
  Knowledge(16, p_id=1, t_id=16),
  Knowledge(17, p_id=1, t_id=17),
  Knowledge(18, p_id=1, t_id=18),
  Knowledge(19, p_id=1, t_id=19),
  Knowledge(20, p_id=1, t_id=20),
  Knowledge(21, p_id=1, t_id=21),
  Knowledge(22, p_id=1, t_id=22),
  Knowledge(23, p_id=1, t_id=23),
  Knowledge(24, p_id=1, t_id=24),
  Knowledge(25, p_id=1, t_id=25),
  Knowledge(26, p_id=1, t_id=26)
]