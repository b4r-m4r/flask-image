from flask import Flask, render_template_string
import docker

app = Flask(__name__)
docker_client = docker.from_env()

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Running Docker Containers</title>
</head>
<body>
    <h1>Running Docker Containers</h1>
    {% if containers %}
        <table border="1">
            <thead>
                <tr>
                    <th>Container ID</th>
                    <th>Name</th>
                    <th>Command</th>
                    <th>Image</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for container in containers %}
                <tr>
                    <td>{{ container['id'] }}</td>
                    <td>{{ container['name'] }}</td>
                    <td>{{ container['command'] }}</td>
                    <td>{{ container['image'] }}</td>
                    <td>{{ container['status'] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p>No running containers found.</p>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def list_containers():
    try:
        containers = docker_client.containers()
        container_data = [
            {
                'id': container["Id"],
                'name': container["Names"][0],
                'command': container["Command"],
                'image': container["Image"],
                'status': container["Status"]
            }
            for container in containers
        ]

        return render_template_string(html_template, containers=container_data)
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)