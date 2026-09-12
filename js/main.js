document.addEventListener('DOMContentLoaded', () => {
    const sseLog = document.getElementById('sse-log');
    const connectionStatus = document.getElementById('connection-status');
    const testBtn = document.getElementById('test-broadcast-btn');

    const API_BASE_URL = 'https://aeronewsfra-api-su5od3qfsq-uc.a.run.app/api/v1';
    const SSE_ENDPOINT = `${API_BASE_URL}/status-stream`;
    const BROADCAST_ENDPOINT = `${API_BASE_URL}/broadcast`;

    function logMessage(message, type = 'info') {
        const li = document.createElement('li');
        li.textContent = message;
        li.className = `log-${type}`;
        sseLog.appendChild(li);
        // Auto-scroll
        sseLog.scrollTop = sseLog.scrollHeight;
    }

    logMessage('Initialisiere SSE-Verbindung...', 'system');
    const eventSource = new EventSource(SSE_ENDPOINT);

    eventSource.onopen = () => {
        connectionStatus.textContent = 'Verbunden';
        connectionStatus.className = 'connected';
        logMessage('SSE-Verbindung hergestellt.', 'system');
    };

    eventSource.onerror = (err) => {
        console.error('EventSource failed:', err);
        connectionStatus.textContent = 'Getrennt';
        connectionStatus.className = 'disconnected';
        logMessage('SSE-Verbindung getrennt oder fehlgeschlagen.', 'error');
        eventSource.close();
    };

    eventSource.onmessage = (event) => {
        const data = JSON.parse(event.data);
        logMessage(`[${data.source}] ${data.message}`);
    };

    testBtn.addEventListener('click', () => {
        logMessage('Sende Test-Broadcast...', 'system');
        fetch(BROADCAST_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: 'Test-Broadcast from Dashboard' }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            logMessage(`Broadcast-Antwort: ${data.detail}`, 'system');
        })
        .catch(error => {
            console.error('Broadcast error:', error);
            logMessage(`Broadcast fehlgeschlagen: ${error.message}`, 'error');
        });
    });
});