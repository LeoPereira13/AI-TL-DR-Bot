import { useState } from 'react';


function App() {
  const [inputText, setInputText] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);

  // Função para enviar o texto para o back-end
  const handleSummarize = async () => {
    if (!inputText.trim()) return;

    setLoading(true);
    setSummary('');

    try {
      const response = await fetch('http://127.0.0.1:5000/summarize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: inputText }),
      });

      const data = await response.json();
      setSummary(data.resumo || 'Erro ao gerar resumo.')

    } catch (error) {
      setSummary('Erro de conexão com a API.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 800, margin: '2rem auto', padding: '1rem' }}>
      <h1>🧠 AI TL;DR Bot</h1>
      <textarea
        rows={10}
        style={{ width: '100%', marginBottom: '1rem' }}
        placeholder="Cole o texto que deseja resumir..."
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button onClick={handleSummarize} disabled={loading}>
        {loading ? 'Resumindo...' : 'Resumir'}
      </button>

      {summary && (
        <div style={{ marginTop: '2rem', background: '#f9f9f9', padding: '1rem', borderRadius: '8px' }}>
          <h3>Resumo:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
