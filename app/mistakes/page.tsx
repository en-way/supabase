"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { 
  getLocalState, 
  toggleMistakeMastered, 
  removeMistake, 
  MistakeItem 
} from "@/lib/storage";
import { 
  AlertCircle, 
  CheckCircle2, 
  XCircle, 
  RotateCcw, 
  Trash2, 
  Printer, 
  Download, 
  Sparkles, 
  HelpCircle,
  BookOpen
} from "lucide-react";

export default function MistakesPage() {
  const [mistakes, setMistakes] = useState<MistakeItem[]>([]);
  const [activeTab, setActiveTab] = useState<"unmastered" | "mastered">("unmastered");
  const [categoryFilter, setCategoryFilter] = useState<string>("all");

  // Re-practice interactive state: { [qId]: selectedKey }
  const [retestAnswers, setRetestAnswers] = useState<Record<string, string>>({});
  // Congratulatory prompt for mastered: qId
  const [congratsId, setCongratsId] = useState<string | null>(null);

  // Print mode toggle: 'exam' (questions only) vs 'solution' (with answer & explanation)
  const [printWithAnswers, setPrintWithAnswers] = useState(true);

  useEffect(() => {
    loadMistakes();
  }, []);

  const loadMistakes = () => {
    const state = getLocalState();
    setMistakes(state.mistakes || []);
  };

  const handleToggle = (qId: string) => {
    toggleMistakeMastered(qId);
    loadMistakes();
  };

  const handleDelete = (qId: string) => {
    if (window.confirm("确定将这道错题从错题本中移除吗？")) {
      removeMistake(qId);
      loadMistakes();
    }
  };

  const handleRetestOption = (item: MistakeItem, optionKey: string) => {
    setRetestAnswers((prev) => ({ ...prev, [item.questionId]: optionKey }));

    if (optionKey === item.correctAnswer) {
      setCongratsId(item.questionId);
    }
  };

  const handleConfirmMastered = (qId: string) => {
    toggleMistakeMastered(qId, true);
    setCongratsId(null);
    loadMistakes();
  };

  // Export as Plain Text File (.txt)
  const handleExportTxt = () => {
    const targetList = filteredMistakes;
    if (targetList.length === 0) {
      alert("当前列表暂无错题可导出");
      return;
    }

    let textContent = `===============================\n`;
    textContent += `Enway 英语智能错题练习集 (${new Date().toLocaleDateString()})\n`;
    textContent += `总计错题: ${targetList.length} 道\n`;
    textContent += `===============================\n\n`;

    targetList.forEach((item, idx) => {
      textContent += `【第 ${idx + 1} 题】(错误次数: ${item.wrongCount})\n`;
      textContent += `${item.stem}\n\n`;
      item.options.forEach((opt) => {
        textContent += `  ${opt.key}. ${opt.text}\n`;
      });
      textContent += `\n[正确答案]: ${item.correctAnswer}\n`;
      textContent += `[上次选错]: ${item.wrongAnswer}\n`;
      textContent += `[考点解析]: ${item.explanation}\n`;
      textContent += `--------------------------------------------------\n\n`;
    });

    const blob = new Blob([textContent], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `Enway_错题本_${new Date().toISOString().slice(0, 10)}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const filteredMistakes = mistakes
    .filter((m) => activeTab === "unmastered" ? !m.isMastered : m.isMastered)
    .filter((m) => categoryFilter === "all" ? true : m.categoryId === categoryFilter);

  return (
    <div className="space-y-6">
      {/* Header Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-white p-6 rounded-2xl border border-slate-200/90 shadow-sm no-print">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center font-bold">
            <AlertCircle className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-slate-900">智能错题本</h1>
            <p className="text-xs text-slate-500 mt-0.5">
              做错自动归集 · 支持重练自测 · 支持纸质打印与纯文本导出
            </p>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex items-center space-x-2">
          <button
            onClick={handleExportTxt}
            className="px-3 py-2 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-50 text-xs font-semibold flex items-center space-x-1.5 transition-colors"
          >
            <Download className="w-3.5 h-3.5 text-slate-500" />
            <span>导出 TXT</span>
          </button>
          <button
            onClick={() => window.print()}
            className="px-3.5 py-2 rounded-xl bg-slate-900 text-white hover:bg-slate-800 text-xs font-semibold flex items-center space-x-1.5 shadow-sm transition-colors"
          >
            <Printer className="w-3.5 h-3.5" />
            <span>打印 / 导出 PDF</span>
          </button>
        </div>
      </div>

      {/* Filter Tabs & Print Settings */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-200 pb-3 no-print">
        <div className="flex items-center space-x-2">
          <button
            onClick={() => setActiveTab("unmastered")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
              activeTab === "unmastered"
                ? "bg-amber-500 text-white shadow-sm"
                : "text-slate-600 hover:bg-slate-100"
            }`}
          >
            待复习 ({mistakes.filter((m) => !m.isMastered).length})
          </button>
          <button
            onClick={() => setActiveTab("mastered")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
              activeTab === "mastered"
                ? "bg-emerald-600 text-white shadow-sm"
                : "text-slate-600 hover:bg-slate-100"
            }`}
          >
            已掌握归档 ({mistakes.filter((m) => m.isMastered).length})
          </button>
        </div>

        {/* Print Options */}
        <div className="flex items-center space-x-2 text-xs text-slate-600">
          <span className="text-slate-400">打印视图:</span>
          <button
            onClick={() => setPrintWithAnswers(!printWithAnswers)}
            className={`px-2.5 py-1 rounded-lg border text-xs font-medium ${
              printWithAnswers ? "bg-indigo-50 border-indigo-200 text-indigo-700" : "bg-white border-slate-200"
            }`}
          >
            {printWithAnswers ? "含答案与解析" : "仅题目(做题卷)"}
          </button>
        </div>
      </div>

      {/* Printable Heading (Only visible in Print) */}
      <div className="hidden print-only text-center mb-6">
        <h1 className="text-2xl font-black mb-1">Enway 英语重点错题复习卷</h1>
        <p className="text-xs text-slate-500">
          打印时间: {new Date().toLocaleDateString()} · 共 {filteredMistakes.length} 道错题
        </p>
      </div>

      {/* Mistakes List */}
      {filteredMistakes.length === 0 ? (
        <div className="text-center py-20 bg-white rounded-2xl border border-dashed border-slate-300 no-print">
          <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
          <p className="text-slate-600 font-medium">太棒了！当前分类下没有待复习错题</p>
          <Link href="/" className="inline-block mt-4 px-4 py-2 bg-indigo-600 text-white text-xs font-semibold rounded-xl">
            前往试卷大厅刷题
          </Link>
        </div>
      ) : (
        <div className="space-y-4">
          {filteredMistakes.map((item, idx) => {
            const retestAns = retestAnswers[item.questionId];
            const isRetested = Boolean(retestAns);
            const isRetestCorrect = retestAns === item.correctAnswer;
            const isShowCongrats = congratsId === item.questionId;

            return (
              <div
                key={item.questionId}
                className="bg-white rounded-2xl border border-slate-200/90 p-6 shadow-sm print-card space-y-4"
              >
                {/* Header info */}
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <span className="px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-900 text-white">
                      错题 #{idx + 1}
                    </span>
                    <span className="text-xs text-rose-600 font-semibold bg-rose-50 px-2 py-0.5 rounded">
                      做错 {item.wrongCount} 次
                    </span>
                    <span className="text-xs text-slate-400 hidden sm:inline">
                      (上次选错: {item.wrongAnswer})
                    </span>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center space-x-2 no-print">
                    <button
                      onClick={() => handleToggle(item.questionId)}
                      className={`px-3 py-1.5 rounded-lg text-xs font-semibold border transition-all ${
                        item.isMastered
                          ? "bg-slate-100 text-slate-600 hover:bg-slate-200"
                          : "bg-emerald-50 border-emerald-200 text-emerald-700 hover:bg-emerald-100"
                      }`}
                    >
                      {item.isMastered ? "撤销已掌握" : "标记已掌握"}
                    </button>
                    <button
                      onClick={() => handleDelete(item.questionId)}
                      title="彻底删除"
                      className="p-1.5 text-slate-400 hover:text-rose-600 rounded-lg hover:bg-rose-50 transition-colors"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>

                {/* Question Stem */}
                <h3 className="text-base font-bold text-slate-900 leading-relaxed">
                  {item.stem}
                </h3>

                {/* Options (Interactive for retesting) */}
                <div className="space-y-2">
                  {item.options.map((opt) => {
                    const isSelected = retestAns === opt.key;
                    const isTheCorrect = opt.key === item.correctAnswer;

                    let optStyle = "bg-slate-50 border-slate-200 text-slate-800 hover:bg-slate-100";
                    if (isRetested) {
                      if (isTheCorrect) {
                        optStyle = "bg-emerald-50 border-emerald-400 text-emerald-950 font-bold";
                      } else if (isSelected) {
                        optStyle = "bg-rose-50 border-rose-300 text-rose-950 font-bold";
                      }
                    }

                    return (
                      <button
                        key={opt.key}
                        onClick={() => handleRetestOption(item, opt.key)}
                        className={`w-full p-3 rounded-xl border text-left flex items-start space-x-3 transition-all ${optStyle}`}
                      >
                        <span className="w-6 h-6 rounded-lg bg-white border border-slate-200 text-xs font-bold flex items-center justify-center shrink-0">
                          {opt.key}
                        </span>
                        <span className="text-xs sm:text-sm pt-0.5">{opt.text}</span>
                      </button>
                    );
                  })}
                </div>

                {/* Retest Success Notification */}
                {isShowCongrats && (
                  <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-xl flex items-center justify-between text-xs text-emerald-800 animate-in fade-in duration-150 no-print">
                    <span className="font-bold">🎉 重做答对了！该题已攻克，是否移入“已掌握”？</span>
                    <button
                      onClick={() => handleConfirmMastered(item.questionId)}
                      className="px-3 py-1 bg-emerald-600 text-white font-bold rounded-lg shadow-sm hover:bg-emerald-700"
                    >
                      移入已掌握
                    </button>
                  </div>
                )}

                {/* Explanation Block (controlled by printWithAnswers during print) */}
                {(printWithAnswers || isRetested) && (
                  <div className={`p-4 rounded-xl bg-slate-50 border border-slate-200/80 text-xs space-y-1.5 ${!printWithAnswers ? 'no-print' : ''}`}>
                    <div className="flex items-center space-x-2 font-bold text-indigo-700">
                      <HelpCircle className="w-3.5 h-3.5" />
                      <span>正确答案: {item.correctAnswer} · 考点精析</span>
                    </div>
                    <p className="text-slate-700 leading-relaxed whitespace-pre-line">
                      {item.explanation}
                    </p>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
