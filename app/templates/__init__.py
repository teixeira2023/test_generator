<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Processador de Arquivos</title>
</head>
<body>
    <h1>Envie um Arquivo .txt</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" accept=".txt" required>
        <button type="submit">Processar</button>
    </form>
    
    {% if frases %}
        <h2>Frases Filtradas</h2>
        <ul>
            {% for frase in frases %}
                <li>{{ frase }}</li>
            {% endfor %}
        </ul>
        <h2>Estatísticas</h2>
        <p>Total de frases: {{ stats.total }}</p>
        <p>Frases removidas: {{ stats.removidas }}</p>
        <p>Frases finais: {{ stats.finais }}</p>
    {% endif %}
</body>
</html>
