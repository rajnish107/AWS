
### ✅ Common Troubleshooting Checklist

- [ ] **Security Group Issues:** Ensure correct inbound rules (e.g., port 80 for HTTP) are set in the instance and Load Balancer security groups.
- [ ] **Instance Health Checks Failing:** Verify the health check path and that the application is running properly on the instances.
- [ ] **Target Group Not Receiving Traffic:** Make sure instances are registered and showing as healthy in the target group.
- [ ] **Load Balancer DNS Not Working:** Confirm the load balancer is in the "active" state and DNS name is correct.
- [ ] **IAM Permissions Errors:** Check IAM roles and policies attached to EC2/Auto Scaling have required permissions.
- [ ] **Auto Scaling Not Triggering:** Review scaling policies, alarms, and ensure CloudWatch metrics are being generated.
- [ ] **User Data Script Not Executing:** Check instance logs (e.g., `/var/log/cloud-init.log`) for script errors or misconfigurations.
- [ ] **EBS Volume Not Attached:** Confirm volume is in the same availability zone and properly attached to the instance.
- [ ] **DNS Caching Issues:** Try clearing browser DNS cache or test the DNS with a different network/device.
- [ ] **Application Not Starting:** Ensure application dependencies are installed and startup commands in user data are correct.
