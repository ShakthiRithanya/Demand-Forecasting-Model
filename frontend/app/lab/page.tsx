"use client";

import React from 'react';
import {
    BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
    Cell
} from 'recharts';

const skuData = [
    { sku: 'PROD-001', accuracy: 98.2 },
    { sku: 'PROD-002', accuracy: 96.5 },
    { sku: 'PROD-003', accuracy: 94.1 },
    { sku: 'PROD-004', accuracy: 89.2 },
    { sku: 'PROD-005', accuracy: 78.4 },
];

export default function ModelLab() {
    return (
        <div className="min-h-screen bg-black text-slate-200 p-8 font-sans">
            <div className="max-w-7xl mx-auto">
                <h1 className="text-3xl font-bold mb-8">Model Performance Lab</h1>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
                    {['Prophet', 'XGBoost', 'LSTM'].map((model) => (
                        <div key={model} className="bg-slate-900 border border-slate-800 p-6 rounded-2xl">
                            <div className="flex justify-between items-center mb-4">
                                <span className="text-sm font-semibold text-slate-400">{model} Forecaster</span>
                                <span className="text-xs px-2 py-0.5 bg-indigo-500/20 text-indigo-400 rounded-full border border-indigo-500/30">Active</span>
                            </div>
                            <div className="text-3xl font-bold mb-2">92.4%</div>
                            <p className="text-xs text-slate-500">WAPE Reduction: +4.2%</p>
                        </div>
                    ))}
                </div>

                <div className="bg-slate-900 border border-slate-800 p-8 rounded-3xl">
                    <h2 className="text-xl font-semibold mb-6">In-Production Model Comparison (WAPE)</h2>
                    <div className="h-80 w-full">
                        <ResponsiveContainer width="100%" height="100%">
                            <BarChart data={skuData}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                                <XAxis dataKey="sku" stroke="#64748b" fontSize={12} tickLine={false} axisLine={false} />
                                <YAxis stroke="#64748b" fontSize={12} tickLine={false} axisLine={false} />
                                <Tooltip
                                    contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px' }}
                                />
                                <Bar dataKey="accuracy" radius={[4, 4, 0, 0]}>
                                    {skuData.map((entry, index) => (
                                        <Cell key={`cell-${index}`} fill={entry.accuracy > 90 ? '#6366f1' : '#f43f5e'} />
                                    ))}
                                </Bar>
                            </BarChart>
                        </ResponsiveContainer>
                    </div>
                </div>
            </div>
        </div>
    );
}
