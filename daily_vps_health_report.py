import psutil
import smtplib
import os
from datetime import datetime
from email.message import EmailMessage
import matplotlib.pyplot as plt

# =========================
# EMAIL CONFIGURATION
# =========================
EMAIL_ADDRESS = "example@gmail.com"
EMAIL_PASSWORD = "xxxx xxxx xxxx xxxx"  # Gmail App Password

FROM_ALIAS = "Example Support <example@gmail.com>"
TO_EMAIL = "example@gmail.com"
CC_EMAILS = ["example@gmail.com"]

# =========================
# FILE PATHS
# =========================
CPU_CHART = "cpu_usage.png"
MEM_CHART = "memory_usage.png"

# =========================
# COLLECT SYSTEM METRICS
# =========================
def collect_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    load_avg = psutil.getloadavg()
    cores = psutil.cpu_count()
    users = psutil.users()

    return {
        "cpu_usage": cpu_usage,
        "memory_used": memory.percent,
        "memory_total": round(memory.total / (1024 ** 3), 2),
        "load_avg": load_avg,
        "cores": cores,
        "users": len(users),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# =========================
# GENERATE CHARTS (EMAIL SAFE)
# =========================
def generate_charts(metrics):
    # CPU Chart
    plt.figure()
    plt.bar(["CPU Usage"], [metrics["cpu_usage"]])
    plt.ylim(0, 100)
    plt.title("CPU Usage (%)")
    plt.savefig(CPU_CHART)
    plt.close()

    # Memory Chart
    plt.figure()
    plt.bar(["Memory Usage"], [metrics["memory_used"]])
    plt.ylim(0, 100)
    plt.title("Memory Usage (%)")
    plt.savefig(MEM_CHART)
    plt.close()

# =========================
# SEND EMAIL
# =========================
def send_email(metrics):
    msg = EmailMessage()
    msg["Subject"] = "Daily VPS Health Report – Hetzner Server"
    msg["From"] = FROM_ALIAS
    msg["To"] = TO_EMAIL
    msg["Cc"] = ", ".join(CC_EMAILS)
    

    health_status = "🟢 Healthy"
    if metrics["cpu_usage"] > 80 or metrics["memory_used"] > 80:
        health_status = "🔴 Attention Required"

    html_body = f"""
    <html>
    <body style="font-family:Arial;background:#f4f4f4;padding:20px;">
      <table width="600" align="center" style="background:#fff;border-radius:8px;padding:20px;">
        <tr>
          <td>
            <h2>Daily VPS Health Report</h2>
            <p><strong>Status:</strong> {health_status}</p>
            <p><strong>Generated:</strong> {metrics["timestamp"]}</p>

            <h3>System Summary</h3>
            <table width="100%" cellpadding="8" cellspacing="0" border="1">
              <tr><td>CPU Usage</td><td>{metrics["cpu_usage"]}%</td></tr>
              <tr><td>Memory Usage</td><td>{metrics["memory_used"]}%</td></tr>
              <tr><td>Total RAM</td><td>{metrics["memory_total"]} GB</td></tr>
              <tr><td>CPU Cores</td><td>{metrics["cores"]}</td></tr>
              <tr><td>Load Average</td><td>{metrics["load_avg"]}</td></tr>
              <tr><td>Active Users</td><td>{metrics["users"]}</td></tr>
            </table>

            <h3>CPU Usage</h3>
            <img src="cid:cpu_chart" width="500">

            <h3>Memory Usage</h3>
            <img src="cid:mem_chart" width="500">

            <p>If you need assistance, please reply to this email.</p>
            <p>Regards,<br><strong>GlobeSign Support Team</strong></p>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """

    msg.set_content("Daily VPS Health Report attached.")
    msg.add_alternative(html_body, subtype="html")

    # Attach images inline
    with open(CPU_CHART, "rb") as f:
        msg.get_payload()[1].add_related(
            f.read(), maintype="image", subtype="png", cid="cpu_chart"
        )

    with open(MEM_CHART, "rb") as f:
        msg.get_payload()[1].add_related(
            f.read(), maintype="image", subtype="png", cid="mem_chart"
        )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("✅ Daily VPS health report email sent")

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    metrics = collect_metrics()
    generate_charts(metrics)
    send_email(metrics)


