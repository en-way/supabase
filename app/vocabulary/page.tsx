"use client";

import { useState, useEffect } from "react";
import { getLocalState, removeVocab, addVocab, VocabItem } from "@/lib/storage";
import { lookupWord } from "@/lib/dictionary";
import { 
  Bookmark, 
  Search, 
  Volume2, 
  Trash2, 
  Plus, 
  Download, 
  Printer, 
  Sparkles 
} from "lucide-react";

export default function VocabularyPage() {
  const [vocabList, setVocabList] = useState<VocabItem[]>([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [showAddModal, setShowAddModal] = useState(false);
  const [newWord, setNewWord] = useState("");
  const [newTranslation, setNewTranslation] = useState("");

  useEffect(() => {
    loadVocab();
  }, []);

  const loadVocab = () => {
    const state = getLocalState();
    setVocabList(state.vocabulary || []);
  };

  const handleDelete = (word: string) => {
    if (window.confirm(`确定从生词本中移除单词 "${word}" 吗？`)) {
      removeVocab(word);
      loadVocab();
    }
  };

  const handleSpeak = (word: string) => {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) return;
    const u = new SpeechSynthesisUtterance(word);
    u.lang = "en-US";
    window.speechSynthesis.speak(u);
  };

  const handleManualAdd = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newWord.trim()) return;
    const lookup = lookupWord(newWord.trim());
    addVocab(
      newWord.trim(), 
      newTranslation.trim() || lookup?.definition || "自定义词汇", 
      lookup?.phonetic || ""
    );
    setNewWord("");
    setNewTranslation("");
    setShowAddModal(false);
    loadVocab();
  };

  const handleExportTxt = () => {
    if (filteredVocab.length === 0) {
      alert("生词本暂无词汇可导出");
      return;
    }

    let content = `Enway 英语专属生词复习表 (${new Date().toLocaleDateString()})\n\n`;
    filteredVocab.forEach((v, idx) => {
      content += `${idx + 1}. ${v.word} ${v.phonetic ? `[${v.phonetic}]` : ""}\n`;
      content += `   释义: ${v.translation}\n`;
      if (v.context) {
        content += `   例句/上下文: ${v.context}\n`;
      }
      content += `\n`;
    });

    const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `Enway_生词本_${new Date().toISOString().slice(0, 10)}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const filteredVocab = vocabList.filter(
    (v) =>
      v.word.toLowerCase().includes(searchTerm.toLowerCase()) ||
      v.translation.includes(searchTerm)
  );

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-white p-6 rounded-2xl border border-slate-200/90 shadow-sm no-print">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold">
            <Bookmark className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-slate-900">划词生词本</h1>
            <p className="text-xs text-slate-500 mt-0.5">
              篇章阅读双击即可收录 · 支持离线朗读与高频考点复习
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-2">
          <button
            onClick={() => setShowAddModal(true)}
            className="px-3 py-2 rounded-xl bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs font-semibold flex items-center space-x-1.5 transition-colors"
          >
            <Plus className="w-3.5 h-3.5" />
            <span>手动添加</span>
          </button>
          <button
            onClick={handleExportTxt}
            className="px-3 py-2 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-50 text-xs font-semibold flex items-center space-x-1.5 transition-colors"
          >
            <Download className="w-3.5 h-3.5" />
            <span>导出 TXT</span>
          </button>
          <button
            onClick={() => window.print()}
            className="px-3.5 py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800 text-xs font-semibold flex items-center space-x-1.5 shadow-sm transition-colors"
          >
            <Printer className="w-3.5 h-3.5" />
            <span>打印生词单</span>
          </button>
        </div>
      </div>

      {/* Search Bar */}
      <div className="relative max-w-md no-print">
        <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
          <Search className="w-4 h-4" />
        </div>
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="搜索生词或中文释义..."
          className="w-full pl-10 pr-4 py-2 bg-white border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500 shadow-sm"
        />
      </div>

      {/* Printable Heading */}
      <div className="hidden print-only text-center mb-6">
        <h1 className="text-2xl font-black mb-1">Enway 英语生词重点复习表</h1>
        <p className="text-xs text-slate-500">
          总计收录 {filteredVocab.length} 个重点考点词汇
        </p>
      </div>

      {/* Vocabulary Cards Grid */}
      {filteredVocab.length === 0 ? (
        <div className="text-center py-20 bg-white rounded-2xl border border-dashed border-slate-300 no-print">
          <Bookmark className="w-12 h-12 text-slate-300 mx-auto mb-3" />
          <p className="text-slate-500 font-medium text-sm">
            {searchTerm ? "未搜索到匹配生词" : "生词本目前为空"}
          </p>
          <p className="text-xs text-slate-400 mt-1">
            在试卷阅读材料中直接双击任意单词，即可一键加入生词本！
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {filteredVocab.map((item) => (
            <div
              key={item.word}
              className="bg-white rounded-2xl border border-slate-200/90 p-5 shadow-sm hover:border-indigo-200 hover:shadow-md transition-all flex flex-col justify-between print-card"
            >
              <div>
                <div className="flex items-start justify-between">
                  <div className="flex items-center space-x-2">
                    <h3 className="text-lg font-bold text-slate-900 capitalize">
                      {item.word}
                    </h3>
                    <button
                      onClick={() => handleSpeak(item.word)}
                      title="朗读单词"
                      className="p-1 hover:bg-slate-100 text-indigo-600 rounded-lg transition-colors no-print"
                    >
                      <Volume2 className="w-4 h-4" />
                    </button>
                  </div>
                  <button
                    onClick={() => handleDelete(item.word)}
                    title="移除"
                    className="text-slate-300 hover:text-rose-600 p-1 rounded-lg no-print"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>

                {item.phonetic && (
                  <span className="text-xs font-mono text-slate-500 block mt-0.5">
                    {item.phonetic}
                  </span>
                )}

                <p className="mt-3 text-sm text-slate-800 font-medium bg-slate-50 p-2.5 rounded-xl border border-slate-100">
                  {item.translation}
                </p>

                {item.context && (
                  <div className="mt-2.5 text-xs text-slate-500 italic bg-amber-50/40 p-2 rounded-lg border border-amber-100/50">
                    "{item.context.trim()}..."
                  </div>
                )}
              </div>

              <div className="mt-4 pt-3 border-t border-slate-100 text-[10px] text-slate-400 no-print">
                收录于: {new Date(item.addedAt).toLocaleDateString()}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Manual Add Modal */}
      {showAddModal && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl max-w-sm w-full p-6 shadow-2xl space-y-4 animate-in fade-in zoom-in-95 duration-150">
            <h3 className="font-bold text-slate-900 text-base">手动添加生词</h3>
            <form onSubmit={handleManualAdd} className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  英文单词
                </label>
                <input
                  type="text"
                  required
                  value={newWord}
                  onChange={(e) => setNewWord(e.target.value)}
                  placeholder="例如: resilient"
                  className="w-full px-3 py-2 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
              </div>
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  中文释义 (可留空自动识别)
                </label>
                <input
                  type="text"
                  value={newTranslation}
                  onChange={(e) => setNewTranslation(e.target.value)}
                  placeholder="例如: adj. 有弹性的；能复原的"
                  className="w-full px-3 py-2 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
              </div>
              <div className="flex justify-end space-x-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowAddModal(false)}
                  className="px-3 py-2 text-xs font-semibold text-slate-600 hover:bg-slate-100 rounded-xl"
                >
                  取消
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-xs font-semibold bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl shadow-sm"
                >
                  确认添加
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
