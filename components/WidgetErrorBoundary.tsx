"use client";

import React, { Component, ErrorInfo, ReactNode } from "react";
import { AlertCircle, RotateCcw } from "lucide-react";

interface Props {
  children: ReactNode;
  fallbackTitle?: string;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

export class WidgetErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
    error: null,
  };

  public static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error("WidgetErrorBoundary caught an error:", error, errorInfo);
  }

  private handleReset = () => {
    this.setState({ hasError: false, error: null });
  };

  public render() {
    if (this.state.hasError) {
      return (
        <div className="p-4 rounded-2xl bg-rose-50/70 border border-rose-200/80 text-rose-700 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 text-xs shadow-sm my-2">
          <div className="flex items-start gap-2.5">
            <AlertCircle className="w-4 h-4 text-rose-500 mt-0.5 flex-shrink-0" />
            <div>
              <div className="font-bold text-rose-900">
                {this.props.fallbackTitle || "该组件加载异常"}
              </div>
              <div className="text-[11px] text-rose-600/90 font-mono mt-0.5 break-all max-w-md">
                {this.state.error?.message || "发生未知客户端错误"}
              </div>
            </div>
          </div>
          <button
            onClick={this.handleReset}
            className="px-3 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-700 text-white font-medium text-[11px] flex items-center space-x-1 shadow-sm transition-all flex-shrink-0 self-end sm:self-center"
          >
            <RotateCcw className="w-3 h-3" />
            <span>重试加载</span>
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

export default WidgetErrorBoundary;
