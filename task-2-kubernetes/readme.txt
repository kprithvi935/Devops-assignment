THIS IS AN ASSIGNMENT COMPLETED BY PRITHVI KAUSHIK
Step 1: Start Minikube

Step 2: Create Namespaces
kubectl apply -f create-namespaces.yaml

Step 3: Set Up Users and RBAC
#Create Contexts for Users
kubectl config set-context user1-context --namespace=ns-user1 --cluster=minikube --user=minikube

kubectl config set-context user2-context --namespace=ns-user2 --cluster=minikube --user=minikube
#Create Roles and Bindings
kubectl apply -f rbac-roles.yaml

Step 4: Deploy Applications
kubectl apply -f deployments-user1.yaml
kubectl apply -f deployments-user2.yaml

Step5: Create Services for Nginx Deployments
kubectl apply -f services.yaml
kubectl apply -f nginx2-config.yaml (for custom nginx xonfiguration for nginx2)

Step6: Set Network Policies to Restrict Access
kubectl apply -f network-policies.yaml

Step7: For better understanding i have created separate network policies for each user and each namespace to understand allow, restrict, allow-internal policies
# Apply network policies for ns-user1
kubectl apply -f deny-external-8080-ns-user1.yaml
kubectl apply -f allow-internal-8080-ns-user1.yaml
kubectl apply -f allow-all-80-ns-user1.yaml

# Apply network policies for ns-user2
kubectl apply -f deny-external-8080-ns-user2.yaml
kubectl apply -f allow-internal-8080-ns-user2.yaml
kubectl apply -f allow-all-80-ns-user2.yaml

Step8: Use of labels to restric particular user/service 
kubectl get namespaces --show-labels
kubectl label namespace ns-user1 name=ns-user1 --overwrite
kubectl label namespace ns-user2 name=ns-user2 --overwrite
kubectl label pods alpine-pod app=nginx -n ns-user1
kubectl label pods alpine-pod app=nginx -n ns-user2

Step9:Test Network Policy Enforcement 
kubectl --namespace ns-user1 exec -it alpine-pod -- curl http://nginx-service.ns-user2.svc.cluster.local:80 #This will work
kubectl --namespace ns-user1 exec -it alpine-pod -- curl http://nginx-service.ns-user2.svc.cluster.local:8080 # This should fail, demonstrating the network policy is effective.

